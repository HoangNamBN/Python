import os
def image_data(datafolder):
    for folder in os.listdir(datafolder):
        curr_path = os.path.join(datafolder, folder)
        print("Folder: ", curr_path)
        for file in os.listdir(curr_path):
            curr_file = os.path.join(curr_path, file)
            print("Image in folder", curr_path, "là: " , curr_file)

if __name__ == "__main__":
    image_data("Data")