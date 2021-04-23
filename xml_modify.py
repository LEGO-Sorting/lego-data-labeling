import os
from xml.dom import minidom
import xml.etree.ElementTree as ET
from pathlib import Path

DATASET_ROOT_DIR = "actual-dataset-22-04-2021/"
DATA_CLASSES_FILE = './predefined_classes.txt'


def go_through_files():
    for brick_type in os.listdir(DATASET_ROOT_DIR):
        brick_type_path = os.path.join(DATASET_ROOT_DIR, brick_type)

        for catalog_number in os.listdir(brick_type_path):
            catalog_number_path = os.path.join(brick_type_path, catalog_number)
            original_path = os.path.join(catalog_number_path, "original")

            for img in os.listdir(original_path):
                image = os.path.join(original_path, img)
                if str(image).endswith(".xml"):
                    # print(image)
                    change_path_files(image)
                # yield brick_type, catalog_number, image


def change_path_files(xml_image_path):
    tree = ET.parse(xml_image_path)
    tree_root = tree.getroot()

    for elem in tree_root.iter('path'):
        xml_path = Path(xml_image_path)
        elem.text = str(xml_path.with_suffix('.jpg'))
        # print(xml_path.with_suffix('.jpg'))
    tree.write(xml_image_path)


if __name__ == '__main__':
    go_through_files()
