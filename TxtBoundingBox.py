import utils


class TxtBoundingBox:
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    category_name = ""
    absolute_path = ""
    txt_filename = "actual_training_boxes.txt"

    def create_box_line(self):
        return str(str(self.xmin)+','+str(self.ymin)+','+str(self.xmax)+','+str(self.ymax))

    def save_bounding_box(self):
        output_data_train = open(self.txt_filename, "a")
        labels = utils.read_label_ids()
        category_id = labels.index(self.category_name)
        line = str(self.absolute_path) + ' ' + self.create_box_line() + ',' + str(category_id)
        output_data_train.write(line)
        output_data_train.write("\n")
        output_data_train.close()
