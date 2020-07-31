# reusable code of webdriver
# if we want to switch from from one window to another(ex: parent - child)
# we define here the code , so that we can call it multiple times
# mouse_over actions also can be done here, so that we can just call the method names everywhere
from selenium import webdriver
import allure

# to create doc string which can be seen in aur report using the plugin called Shingx, for that we should write in
# """  """
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.action_chains import ActionChains

"""
Author : Prajwal Naresh
Description : To change the focus from parent to child window/tab.
Arguments : Webdriver
Return_Type : None
Exceptions : Throws NoSuchWindowException
"""


@allure.step
def switch_to_child_window(driver):
    child_window = None
    parent_window = driver.current_window_handle
    window_ids = driver.window_handles
    try:
        for window_id in window_ids:
            if window_id != parent_window:
                child_window = window_id
                break
        driver.switch_to.window(child_window)

    except NoSuchWindowException:
        print("Unable to change the focus to child window/tab")

@allure.step
def switch_to_window_using_title(driver, title):
    child_window = None
    window_ids = driver.window_handles
    try:
        for win_id in window_ids:
            driver.switch_to.window(win_id)
            if title != driver.title:
                window_id = win_id
                break
        driver.switch_to.window(window_id)

    except NoSuchWindowException:
        print("Unable to change the focus to child window/tab")


class Actions:
    def __init__(self, driver):
        self.action = ActionChains(driver)

    def move_to_element(self, driver, element):
        self.action.move_to_element(element).perform()

    def right_click(self, element):
        self.action.context_click(element).perform()

    def drag_and_drop(self, source, target):
        self.action.drag_and_drop(source, target).perform()
