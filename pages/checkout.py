from PyQt6.QtWidgets import QMainWindow, QMessageBox
import sys
from PyQt6 import uic
import os
import re

class CheckoutPage(QMainWindow):
    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        # load file ui
        ui_path = self.root_dir + "/ui/checkout.ui"
        uic.loadUi(ui_path, self)


        # bat su kien cho cac nut bam
        self.home.clicked.connect(self.goto_home)
        self.gio_hang.clicked.connect(self.goto_gio_hang)

        # hien thi giao dien
        self.show()

    # ------------------ xu ly su kien ------------------
    def goto_home(self):
        from pages.home import HomePage

        self.home_page = HomePage(
            main_window=self.main_window, root_dir=self.root_dir, cur_acc=self.cur_acc
        )
        self.close()  # ✅ đóng cửa sổ

    def goto_gio_hang(self):
        from pages.gio_hang import GioHangPage

        self.gio_hang_page = GioHangPage(
            main_window=self.main_window, root_dir=self.root_dir, cur_acc=self.cur_acc
        )
        self.close()  # ✅ đóng cửa sổ
    #-------------------ham cho chuc nang chinh-----------------
    def save_to_history(self):
        pass
    def validate_form(self):
        pass
    # ------------------ ham ho tro ------------------
    def show_message(self, message):
        # Khởi tạo hộp thoại thông báo
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(
            QMessageBox.Icon.Information
        )  # Các icon mặc định: Information, Warning, Critical, Question
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)  # Nút bấm OK
        # Hiển thị hộp thoại
        msg.exec()