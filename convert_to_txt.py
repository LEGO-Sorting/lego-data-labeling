import os
import consts
import xml.etree.ElementTree as ET
from TxtBoundingBox import TxtBoundingBox
from pathlib import Path


def read_label_ids():
    label_file = open(consts.DATA_CLASSES_FILE, "r")
    labels = label_file.read().splitlines()
    return labels


def find_boxes_on_single_image(xml_path):
    found_box = TxtBoundingBox()
    path_to_image = os.path.join(Path().absolute(), 'TrainYourOwnYOLO', 'Data', 'Source_Images', 'Training_Images',
                                 xml_path)
    found_box.absolute_path = path_to_image
    tree = ET.parse(xml_path)
    tree_root = tree.getroot()
    print(xml_path)

    for annotation_element in tree_root.iter('object'):
        print('------||------')
        for object_element in annotation_element.iter('bndbox'):
            for x_min in object_element.iter('xmin'):
                print('xmin: ' + x_min.text)
                found_box.xmin = x_min.text
            for y_min in object_element.iter('ymin'):
                print('ymin: ' + y_min.text)
                found_box.ymin = y_min.text
            for x_max in object_element.iter('xmax'):
                print('xmax: ' + x_max.text)
                found_box.xmax = x_max.text
            for y_max in object_element.iter('ymax'):
                print('ymax: ' + y_max.text)
                found_box.ymax = y_max.text

    for category in tree_root.iter('category'):
        print('category: ' + category.text)
        found_box.category_name = category.text

    print('\n')
    found_box.save_bounding_box()


def go_through_files():
    available_categories = read_label_ids()
    for brick_type in os.listdir(consts.ACTUAL_DATASET_ROOT_DIR):
        brick_type_path = os.path.join(consts.ACTUAL_DATASET_ROOT_DIR, brick_type)

        for catalog_number in os.listdir(brick_type_path):
            if catalog_number not in available_categories:
                print("category " + catalog_number + " is not available")
                continue
            catalog_number_path = os.path.join(brick_type_path, catalog_number)
            original_path = os.path.join(catalog_number_path, "original")

            for img in os.listdir(original_path):
                image = os.path.join(original_path, img)
                if str(image).endswith(".xml"):
                    # print(image)
                    find_boxes_on_single_image(image)


if __name__ == '__main__':
    go_through_files()
