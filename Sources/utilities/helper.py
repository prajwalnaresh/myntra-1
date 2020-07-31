# to clear allure-results(json files generated) or to delete any files or to for clearing purpose we use this file

# to keep general utility functions
# assume we have one single method which has to be used, for that we dont have to create,one file
# instead we can write it under this file, those functions can be written here
# also we write one method here to delete the generated json file under directory allure_results
from pathlib import Path
import os
from time import sleep

import allure


def attach_screen_shot(driver, name):
    allure.attach(driver.get_screen_shot_as_png(), name=name,
                  attachment_type=allure.attachment_type.PNG)


# this method is used to take screenshot, when we call the method,
# it calls driver and name
# driver.get_screen_shot_as_png() ismethod used to take screenshot
# name will specify unique name for each sc
# the type of format will be mentioned as PNG

def delete_all_files(directory_path):
    path = Path(directory_path)  # to navigate to file_path
    files = path.iterdir()  # this will iterate and check with all files and delete in that path

    for file in files:  # this will iterate through files
        if file.is_file():  # this will check if file or not, if yes it will delete, else no
            os.remove(file)  # if present it will remove

    sleep(5)
