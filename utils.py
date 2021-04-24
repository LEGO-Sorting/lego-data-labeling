import consts


def read_label_ids():
    label_file = open(consts.DATA_CLASSES_FILE, "r")
    labels = label_file.read().splitlines()
    return labels
