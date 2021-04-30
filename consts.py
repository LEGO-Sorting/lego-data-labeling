import os
from pathlib import Path

DATA_CLASSES_FILE = './predefined_classes.txt'
DATASET_DIR = os.getcwd() + "/TrainYourOwnYOLO/Data/Source_Images/Training_Images/mixed-dataset"
ACTUAL_DATASET_ROOT_DIR = os.path.join(Path().absolute(), 'TrainYourOwnYOLO', 'Data', 'Source_Images', 'Training_Images',
                                       "actual-dataset-22-04-2021/")
