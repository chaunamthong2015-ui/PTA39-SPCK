from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from PyQt6 import uic
import os

# from pages.login import LoginPage # trang dau tien truy cap
from pages.home import HomePage 
from entities.user import User



# lay duong dan den cac file con
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# chi chay khi run bang app.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    curuser = User(username="admin", email="admin@gmail.com", password="123456")
    first_page = HomePage(main_window=None, root_dir=BASE_DIR, cur_acc=curuser)
    sys.exit(app.exec())