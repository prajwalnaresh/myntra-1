# runnable file with pytest main method
from datetime import datetime
from time import sleep

import pytest
import os
from Sources.utilities import globals, helper


class ReportPlugin:

    def pytest_sessionfinish(self):
        globals.ALLURE_REPORT = globals.ALLURE_REPORT + datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        os.popen("allure generate " + globals.ALLURE_RESULTS + " --output " + globals.ALLURE_REPORT)


# Deleting the Json files which are created.
sleep(15)
helper.delete_all_files(globals.ALLURE_RESULTS)



args = ['-s', '-v', '--alluredir', globals.ALLURE_RESULTS]
pytest.main(args, plugins=[ReportPlugin()])
