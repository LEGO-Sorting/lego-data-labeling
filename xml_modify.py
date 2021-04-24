import os
import utils
import consts


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
                        utils.change_path_files(image)
                        utils.add_category(image, "unknown")
                        continue
                    utils.change_path_files(image)
                    utils.add_category(image, catalog_number)


if __name__ == '__main__':
    go_through_files()
