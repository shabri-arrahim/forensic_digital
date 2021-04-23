import os
import sys

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), "../"))

from PyQt5 import QtCore, QtGui, QtWidgets

from view.main_view import Ui_MainWindow
from helpers.log_parser import Logger
from libs.forensic_digital import AdbSetup

log = Logger().get_logger()

class MainController():
    @classmethod
    def run(self):
        adb = AdbSetup()
        app = QtWidgets.QApplication(sys.argv)
        
        MainWindow = QtWidgets.QMainWindow()
        
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        
        if adb.get_device() is not None:
            ui.set_table_item(adb.get_device_information())
            log.info(adb.get_package_list())
            list_package = adb.get_package_list()
            ui.set_list_log(list_package)
            # ui.set_btn_backup_listener(adb.backup())
            # ui.set_btn_inspect_listener(list_package)
        
        MainWindow.show()
        
        sys.exit(app.exec_())