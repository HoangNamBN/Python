from flask import Flask, render_template, request
import os
import pickle
import numpy as np
from api_models import face_recognition
from PIL import Image, ImageDraw

'''Khởi tạo model đã train'''
file = open("models/svm_means_test.dat", 'rb')
clf, means, names = pickle.load(file)

# khởi tạo Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"


# xử lý các request
@app.route("/", methods=["POST", "GET"])
def home():
    # Nếu là GET request thì hiển thị ra giao diện
    if request.method == "GET":
        return render_template("index.html")
    else:
        '''1. Lấy file mà client upload lên'''
        global CountDetect
        image_file = request.files['file']
        if image_file:
            print(image_file.filename)
            print(app.config['UPLOAD_FOLDER'])
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            print("Save = ", path_to_save)
            image_file.save(path_to_save)

            pil_image = Image.open(image_file).convert("RGB")
            draw = ImageDraw.Draw(pil_image)

            X_img = face_recognition.load_image_file(image_file)
            X_face_locations = face_recognition.face_locations(X_img)
            if len(X_face_locations) == 0:
                return []
            faces_encodings = face_recognition.face_encodings(X_img, X_face_locations)
            namess = ""
            for (top, right, bottom, left), face_encoding in zip(X_face_locations, faces_encodings):
                matches = face_recognition.compare_faces(means, face_encoding)
                name = "unknown"
                face_distance = face_recognition.face_distance(means, face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = names[best_match_index]
                draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))
                name = name.encode("UTF-8")
                nameout = str(name).replace("b'", "").replace("'", "")
                namess += nameout + " "

            del draw
            return render_template("index.html", user_image = image_file.filename,
                                   msg = "Tải file lên thành công", namess=namess, hasface = True)
        else:
            return render_template('index.html', msg='Hãy chọn file để tải lên')
# start server
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
