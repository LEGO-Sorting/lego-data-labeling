import csv
import os
import consts
import utils


def write_serialized_csv(serialized_data):
    with open(consts.SERIALIZED_TEST_RESULTS_PATH, "w+") as my_csv:
        csv_writer = csv.writer(my_csv, delimiter=',')
        csv_writer.writerows(serialized_data)


def check_decision(label, image_name):
    return label in os.path.basename(image_name)


def serialize_test_results():
    csv_file = open(consts.TEST_RESULTS_PATH, 'r+')
    reader = csv.reader(csv_file)
    training_categories = utils.read_label_ids()
    detected_objects = []

    for row in reader:
        detected_objects.append(row)

    print(len(detected_objects))

    for row in detected_objects:
        if row[6] == 'label':
            row.append('decision')
            continue
        category_index = int(row[6])
        category = training_categories[category_index]
        row[6] = category
        row.append('HIT' if check_decision(category, row[0]) else 'MISS')
    print(detected_objects)
    write_serialized_csv(detected_objects)
    csv_file.close()


if __name__ == '__main__':
    serialize_test_results()
