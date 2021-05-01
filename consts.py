import os
from pathlib import Path

DATA_CLASSES_FILE = './predefined_classes.txt'
DATASET_DIR = os.getcwd() + "/TrainYourOwnYOLO/Data/Source_Images/Training_Images/mixed-dataset"
TEST_RESULTS_PATH = os.getcwd() + \
                    "/TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results/Detection_Results.csv"
SERIALIZED_TEST_RESULTS_PATH = os.getcwd() + \
                    "/TrainYourOwnYOLO/Data/Source_Images/Test_Image_Detection_Results/Serialized_Detection_Results.csv"
TRAINING_DATA_CLASSES = os.getcwd() + \
                    "/TrainYourOwnYOLO/Data/Source_Images/Training_Images/vott-csv-export/data_classes.txt"
ACTUAL_DATASET_ROOT_DIR = os.path.join(Path().absolute(), 'TrainYourOwnYOLO', 'Data', 'Source_Images', 'Training_Images',
                                       "actual-dataset-22-04-2021/")

