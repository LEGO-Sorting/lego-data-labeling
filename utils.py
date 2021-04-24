import consts
import xml.etree.ElementTree as ET
from pathlib import Path


def read_label_ids():
    label_file = open(consts.DATA_CLASSES_FILE, "r")
    labels = label_file.read().splitlines()
    return labels


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
