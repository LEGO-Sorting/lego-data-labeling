import utils


class TxtBoundingBox:
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    category_name = ""
    relative_path = ""
    txt_filename = "actual_training_boxes.csv"

    def __init__(self, relative_path, x_min, y_min, x_max, y_max, category_name):
        self.xmin = x_min
        self.ymin = y_min
        self.xmax = x_max
        self.ymax = y_max
        self.relative_path = relative_path
        self.category_name = category_name

    def create_box_line(self):
        return str(self.xmin+','+self.ymin+','+self.xmax+','+self.ymax)

    def save_bounding_box(self):
        output_data_train = open(self.txt_filename, "w")
        labels = utils.read_label_ids()
        category_id = labels.index(self.category_name)
        line = str(self.relative_path) + ' ' + self.create_box_line() + ',' + str(category_id)
        output_data_train.write(line)
        output_data_train.write("\n")
        output_data_train.close()
