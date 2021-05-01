import csv
import consts
import utils


def serialize_test_results():
    csv_file = open(consts.TEST_RESULTS_PATH, 'r')
    reader = csv.reader(csv_file)
    training_categories = utils.read_label_ids()
    detected_objects = []

    for row in reader:
        detected_objects.append(row)

    print(len(detected_objects))

    for row in detected_objects:
        if row[6] == 'label':
            continue
        category_index = int(row[6])
        # row[6] = training_categories[row[6].__getitem__()]
        row[6] = training_categories[category_index]
    print(detected_objects)

    csv_file.close()


if __name__ == '__main__':
    serialize_test_results()
