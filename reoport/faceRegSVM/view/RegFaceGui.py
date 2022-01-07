from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter
from api_models import face_recognition
import os.path
import time
import os
from sklearn import svm
import pickle
import numpy as np
from PIL import Image, ImageDraw, ImageTk
from faceRegSVM.process.DataProcessing import image_data, SaveImage
from api_models.face_recognition.face_recognition_cli import image_files_in_folder

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'PNG', "JPG"}
CountDetect = 0
path_train = "../data/faceTrain"
path_test = "../data/faceTest"
model_save_path = "../models/svm_means_test.dat"
ImageOut = "../data/Out"

''' font chữ cho giao diện '''
large_font = ('Verdana', 25, "bold")
small_font = ('Verdana', 10)

''' Tạo lớp giao diện '''
root = tkinter.Tk()


class Form(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initialize_interface()
    def initialize_interface(self):
        self.parent.title("Face SVM")
        # self.parent.config(background="lavender")
        self.parent.geometry("800x650")
        self.parent.resizable(False, False)

        '''khai báo các biến toàn cục sử dụng cho bài toán'''
        global openFolder  # biến dùng để lưu đường dẫn mở folder
        global countTrainImg  # biến dùng để lấy kết quả số lượng ảnh train
        global countTestImg  # biến dùng để lấy kết quả số lượng ảnh test
        global openImage  # biến dùng để lưu kết quả mở ảnh
        global ImgRecognition  # biến dùng để lưu kết quả đường dẫn ảnh được nhận dạng
        global timetrain  # biến dùng để lưu thời gian train 1 ảnh
        global timetest  # biến dùng để lưu thời gian test 1 ảnh
        global namespersion  # biến dùng để lấy ra tên người dùng
        # global img

        ''' dùng các biến để hứng kết quả'''
        openFolder = tkinter.StringVar()
        countTrainImg = tkinter.StringVar()
        countTestImg = tkinter.StringVar()
        openImage = tkinter.StringVar()
        ImgRecognition = tkinter.StringVar()
        timetrain = tkinter.StringVar()
        timetest = tkinter.StringVar()
        namespersion = tkinter.StringVar()

        ''' Tạo tiêu đề '''
        self.lbGui = tkinter.Label(self.parent, text="Recoginition Face with SVM", fg="black", font=large_font)
        self.lbGui.place(x=160, y=15)

        ''' Tạo button mở lấy đường dẫn của folder faceData '''
        self.btnFolder = tkinter.Button(self.parent, text="Open Brower", command=open_folder, fg="black",
                                        font=small_font)
        self.btnFolder.place(x=10, y=70, width=150, height=25)

        ''' Taọ entry hứng kết quả lấy đường dẫn folder '''
        self.entryFolder = tkinter.Entry(self.parent, textvariable=openFolder, width=85, font=small_font)
        self.entryFolder.place(x=180, y=70, height=25)

        ''' Tạo button chia dữ liệu'''
        self.btnResultTrainTest = tkinter.Button(self.parent, text="Split Dataset", fg="black", font=small_font,
                                                 command=Train_Test)
        self.btnResultTrainTest.place(x=10, y=120, width=150, height=25)

        ''' entry lấy kết quả trả về của số lượng ảnh train '''
        self.lbCountTrain = tkinter.Label(self.parent, text="Train ", fg="black", font=small_font)
        self.lbCountTrain.place(x=180, y=120)
        self.entryTrain = tkinter.Entry(self.parent, textvariable=countTrainImg, width=20)
        self.entryTrain.place(x=230, y=115, height=25)
        self.lbFIle = tkinter.Label(self.parent, text="file", fg="black", font=small_font)
        self.lbFIle.place(x=380, y=120)

        ''' entry lấy kết quả trả về của số lượng ảnh test '''
        self.lbCountTest = tkinter.Label(self.parent, text="Test", fg="black", font=small_font)
        self.lbCountTest.place(x=500, y=120)
        self.entryTest = tkinter.Entry(self.parent, textvariable=countTestImg, width=20)
        self.entryTest.place(x=550, y=115, height=25)
        self.lbFIleTest = tkinter.Label(self.parent, text="file", fg="black", font=small_font)
        self.lbFIleTest.place(x=700, y=120)

        ''' Button train dữ liệu '''
        self.btnTrain = tkinter.Button(self.parent, text="Train Models", command=TrainModels)
        self.btnTrain.place(x=10, y=170, width=150, height=25)

        ''' mở ảnh lên để test '''
        self.openfile = tkinter.Button(self.parent, text="Open Image", command=OPenImage)
        self.openfile.place(x=180, y=170, width=150, height=25)

        self.btnRecognition = tkinter.Button(self.parent, text="Detector and Recognition", command=Detector)
        self.btnRecognition.place(x=350, y=170, width=220, height=25)

        self.lbImage = tkinter.Label(self.parent, bd=2, text="Choose photos to check", borderwidth=2, width=20,
                                     height=10, relief="ridge")
        self.lbImage.place(x=10, y=220, width=250, height=250)

        img = Image.open("muiten.png")
        img = img.resize((25, 25), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.lbMuiTen = tkinter.Label(self.parent, image=img, bd=2, borderwidth=2, relief="ridge")
        self.lbMuiTen.image = img
        self.lbMuiTen.place(x=275, y=320)

        self.lbImageReg = tkinter.Label(self.parent, bd=2, text="Recognized photo", borderwidth=2, width=20,
                                        height=10, relief="ridge")
        self.lbImageReg.place(x=320, y=220, width=250, height=250)

        self.lbTitle = tkinter.Label(self.parent, text="Execution Time")
        self.lbTitle.place(x=600, y=220)

        ''' thực hiện lấy thời gian train '''
        self.lbTimeTrain = tkinter.Label(self.parent, bd=2, text="train time: ")
        self.lbTimeTrain.place(x=600, y=260)

        ''' entry hứng kết quả thời gian train dữ liệu '''
        self.entryTimeTrain = tkinter.Entry(self.parent, textvariable=timetrain, width=8)
        self.entryTimeTrain.place(x=690, y=260)

        ''' label số giây '''
        self.lbS = tkinter.Label(self.parent, text="(s)", fg="black", font=small_font)
        self.lbS.place(x=760, y=260)

        ''' thực hiện lấy thời gian test '''
        self.lbTimeTest = tkinter.Label(self.parent, bd=2, text="test time: ")
        self.lbTimeTest.place(x=600, y=300)

        ''' entry hứng kết quả thời gian train dữ liệu '''
        self.entryTimetest = tkinter.Entry(self.parent, textvariable=timetest, width=8)
        self.entryTimetest.place(x=690, y=300)

        ''' label số giây '''
        self.lbSTest = tkinter.Label(self.parent, text="(s)", fg="black", font=small_font)
        self.lbSTest.place(x=760, y=300)

        ''' thực hiện lấy tên ảnh của người cần nhận dạng '''
        self.lbRecoginitionName = tkinter.Label(self.parent, text="Recoginition Face", fg="black", font=small_font)
        self.lbRecoginitionName.place(x=10, y=515)

        ''' Hứng tên kết quả nhận dạng '''
        self.entryNames = tkinter.Entry(self.parent, textvariable=namespersion, width=85, font=small_font)
        self.entryNames.place(x=180, y=510, height=25)

        ''' Đánh dấu tác giả '''
        tkinter.Label(self.parent, text="Electric Power Universtiy - class D13CNPM5", fg="black",
                      font=small_font).place(x=10, y=560)
        tkinter.Label(self.parent, text="Members: Nguyen Van Nam and Ha Quy Duc", fg="black", font=small_font).place(
            x=10, y=590)

def OPenImage():
    x = openfile()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbImage = tkinter.Label(root, image=img, bd=2, borderwidth=2, width=20, height=10, relief="ridge")
    lbImage.image = img
    lbImage.place(x=10, y=220, width=250, height=250)

def openfile():
    filename = filedialog.askopenfilename()
    openImage.set(filename)
    return filename

def open_folder():
    folder = filedialog.askdirectory()
    openFolder.set(folder)
    return openFolder

def Train_Test():
    datafolder = openFolder.get()
    path_train = "../data/faceTrain"
    path_test = "../data/faceTest"
    if not os.path.exists(path_train):
        os.mkdir(path_train)
    if not os.path.exists(path_test):
        os.mkdir(path_test)
    messagebox.showinfo("Notification", "Start Dividing Data")
    X_train, X_test, Y_train, Y_test, path_train, path_test, datafolder = image_data(datafolder, path_train, path_test)
    SaveImage(X_train, X_test, Y_train, Y_test, path_train, path_test)
    countTrainImg.set(len(X_train))
    countTestImg.set(len(X_test))
    print("Dividing faceTrain faceTest Accssuary !")
    messagebox.showinfo("Notification", "Successfully Divided Data")

def TrainModels():
    print("Start faceTrain Models....")
    messagebox.showinfo("Notification", "Start Model Training")
    start = time.time()
    verbose = False
    names = []
    means = []
    for class_dir in os.listdir(path_train):
        encodings = []
        if not os.path.isdir(os.path.join(path_train, class_dir)):
            continue
        for img_path in image_files_in_folder(os.path.join(path_train, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)
            if len(face_bounding_boxes) != 1:
                if verbose:
                    print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(
                        face_bounding_boxes) < 1 else "Found more than one face"))
            else:
                face_encodings = face_recognition.face_encodings(image)[0]
                encodings.append(face_encodings)
                names.append(class_dir)
                means.append([np.mean(x, axis=0) for x in zip(*encodings)])
    clf = svm.SVC(gamma='scale')
    clf.fit(means, names)
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump([clf, means, names], f)
    end = time.time()
    countTrain = countTrainImg.get()
    timetrain.set(round(float(str(end - start)) / float(countTrain), 2))
    print("faceTrain Models Accssuary !")
    messagebox.showinfo("Notification", "Successful model training")
    return clf, means, names

def show_prediction_labels_on_image(X_img_path, path_out, means, names, model_save_path=None, clf=None):
    global CountDetect
    if not os.path.isfile(X_img_path) or os.path.splitext(X_img_path)[1][1:] not in ALLOWED_EXTENSIONS:
        raise Exception("Invalid data path: {}".format(X_img_path))
    if clf is None and model_save_path is None:
        raise Exception("Must supply svm classifier either thourgh knn_clf or model_path")
    pil_image = Image.open(X_img_path).convert("RGB")
    draw = ImageDraw.Draw(pil_image)
    nameout = ""
    X_img = face_recognition.load_image_file(X_img_path)
    start = time.time()
    X_face_locations = face_recognition.face_locations(X_img)
    end = time.time()
    if len(X_face_locations) == 0:
        return []
    CountDetect = CountDetect + len(X_face_locations)
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
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(255, 0, 0), outline=(255, 0, 0))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
        nameout = str(name).replace("b'", "").replace("'", "")
        namess += nameout + " - "
    namespersion.set(namess[:-3])
    del draw
    pil_image.save(path_out)
    timetest.set(round((float(str(end - start)) / CountDetect), 2))
    return nameout

def Detector():
    if os.path.isfile(model_save_path):
        with open(model_save_path, 'rb') as f:
            clf, means, names = pickle.load(f)
    if not os.path.exists(ImageOut):
        os.mkdir(ImageOut)
    CountName = 0
    full_file_path = openImage.get()
    path_out = ImageOut + "/" + os.path.basename(full_file_path)
    name = show_prediction_labels_on_image(full_file_path, path_out, means, names, model_save_path)
    if str(name) == str(os.path.basename(full_file_path).split("_")[0]):
        CountName += 1
    recognition = path_out
    img = Image.open(recognition)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbRecognition=Label(root, image=img, bd=2, borderwidth=2, width=20, height=10, relief="ridge")
    lbRecognition.image = img
    lbRecognition.place(x=320, y=220, width=250, height=250)

def main():
    gui = Form(root)
    gui.mainloop()

if __name__ == "__main__":
    main()
