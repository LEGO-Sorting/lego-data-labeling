from PIL import Image, ImageChops
import os
import utils
import consts


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


def get_images():
    file_names = list_files_recursive(consts.DATASET_DIR)
    file_names.sort()
    return file_names


def construct_training_file():
    output_data_train = open("data_train_labels.txt", "w")
    recordsCount = 1
    image_files = get_images()
    print(len(image_files))
    # print(image_files)
    labels = utils.read_label_ids()

    for image_path in image_files:
        im = Image.open(image_path)
        file_name = os.path.basename(image_path)
        class_string = os.path.splitext(file_name)[0]
        class_number = labels.index(class_string)

        if get_box(im) is None:
            continue
        if recordsCount > len(image_files):
            break
        line = str(image_path) + ' ' + ','.join(map(str, get_box(im))) + ',' + str(class_number)
        output_data_train.write(line)
        output_data_train.write("\n")
        recordsCount = recordsCount + 1
    output_data_train.close()


if __name__ == '__main__':
    print(consts.DATASET_DIR)
    construct_training_file()
    # result = list_files_recursive(os.getcwd() + "/Data/")
    # print(result)