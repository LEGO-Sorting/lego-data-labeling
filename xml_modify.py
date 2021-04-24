import os
import utils
import consts
import xml.etree.ElementTree as ET
from pathlib import Path


def go_through_files():
    available_categories = utils.read_label_ids()
    for brick_type in os.listdir(consts.ACTUAL_DATASET_ROOT_DIR):
        brick_type_path = os.path.join(consts.ACTUAL_DATASET_ROOT_DIR, brick_type)

        for catalog_number in os.listdir(brick_type_path):
            catalog_number_path = os.path.join(brick_type_path, catalog_number)
            original_path = os.path.join(catalog_number_path, "original")

            for img in os.listdir(original_path):
                image = os.path.join(original_path, img)

                if str(image).endswith(".xml"):
                    if catalog_number not in available_categories:
                        print("category " + catalog_number + " is not available. Marked as an unknown.")
                        change_path_files(image)
                        add_category(image, "unknown")
                        continue
                    change_path_files(image)
                    add_category(image, catalog_number)


def add_category(xml_image_path, category):
    tree = ET.parse(xml_image_path)
    tree_root = tree.getroot()
    attrib = {}
    category_element = tree_root.makeelement('category', attrib)
    category_element.text = category

    for elem in tree_root.iter('category'):
        elem.text = str(category)
        tree.write(xml_image_path)
        return
    tree_root.append(category_element)
    tree.write(xml_image_path)


def change_path_files(xml_image_path):
    tree = ET.parse(xml_image_path)
    tree_root = tree.getroot()

    for elem in tree_root.iter('path'):
        xml_path = Path(xml_image_path)
        elem.text = str(xml_path.with_suffix('.jpg'))
    tree.write(xml_image_path)


if __name__ == '__main__':
    go_through_files()
