import os
import xml.etree.ElementTree as ET
from pathlib import Path

DATASET_ROOT_DIR = "actual-dataset-22-04-2021/"
DATA_CLASSES_FILE = './predefined_classes.txt'


def read_label_ids():
    label_file = open(DATA_CLASSES_FILE, "r")
    labels = label_file.read().splitlines()
    return labels


def go_through_files():
    available_categories = read_label_ids()
    for brick_type in os.listdir(DATASET_ROOT_DIR):
        brick_type_path = os.path.join(DATASET_ROOT_DIR, brick_type)

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
                    change_path_files(image)
                    add_category(image, catalog_number)


if __name__ == '__main__':
    go_through_files()
