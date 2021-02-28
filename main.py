from PIL import Image, ImageChops
import os


DATA_CLASSES_FILE = './predefined_classes.txt'
DATASET_DIR = os.getcwd() + "/Data/"


def list_files_recursive(path):
    """
    Function that receives as a parameter a directory path
    :return list_: File List and Its Absolute Paths
    """


    files = []

    # r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if str(file).endswith((".jpg", ".png", ".jpeg")):
                files.append(os.path.join(r, file))

    lst = [file for file in files]
    return lst


def get_box(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    box = diff.getbbox()
    return box


def read_label_ids():
    label_file = open(DATA_CLASSES_FILE, "r")
    labels = label_file.read().splitlines()
    return labels


def get_images():
    file_names = list_files_recursive(DATASET_DIR)
    file_names.sort()
    return file_names


def construct_training_file():
    output_data_train = open("data_train_labels.txt", "w")
    recordsCount = 1
    image_files = get_images()
    print(image_files)
    # labels = read_label_ids()

    for image_path in image_files:
        im = Image.open(image_path)
        label = os.path.basename(image_path)

        if get_box(im) is None:
            continue
        line = image_path + ' ' + ' '.join(map(str, get_box(im))) + ' ' + os.path.splitext(label)[0]
        output_data_train.write(line)
        output_data_train.write("\n")
        recordsCount = recordsCount + 1
    output_data_train.close()


if __name__ == '__main__':
    construct_training_file()
    result = list_files_recursive(os.getcwd() + "/Data/")
    print(result)
