class TxtBoundingBox:
    xmin = 0
    ymin = 0
    xmax = 0
    ymax = 0
    category_name = ""
    relative_path = ""
    csv_filename = "actual_training_boxes.csv"

    def __init__(self, relative_path, x_min, y_min, x_max, y_max, category_name):
        self.xmin = x_min
        self.ymin = y_min
        self.xmax = x_max
        self.ymax = y_max
        self.relative_path = relative_path
        self.category_name = category_name

    def save_into_csv(self):
