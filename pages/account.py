# ==========================================================
# account.py - Trang TÀI KHOẢN (ui/account.ui)
# ==========================================================
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
import os


class TrangTaiKhoan(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "account.ui")
        uic.loadUi(duong_dan_ui, self)

        # hiện thông tin tài khoản
        self.thong_tin_tai_khoan.setText(
            f"Họ tên: {self.tai_khoan.lay_ho_ten()}   |   Email: {self.tai_khoan.lay_email()}"
        )

        # bắt sự kiện cho các nút
        self.nut_trang_chu.clicked.connect(self.chuyen_trang_chu)
        self.nut_gio_hang.clicked.connect(self.chuyen_trang_gio_hang)
        self.nut_lich_su.clicked.connect(self.chuyen_trang_lich_su)
        self.nut_dang_xuat.clicked.connect(self.chuyen_trang_dang_nhap)

        self.show()

    # ------------------ chuyển trang ------------------
    def chuyen_trang_chu(self):
        from pages.home import TrangChu

        self.trang_chu = TrangChu(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    def chuyen_trang_gio_hang(self):
        from pages.gio_hang import TrangGioHang

        self.trang_gio_hang = TrangGioHang(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    def chuyen_trang_lich_su(self):
        from pages.lich_su import TrangLichSu

        self.trang_lich_su = TrangLichSu(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    def chuyen_trang_dang_nhap(self):
        # đăng xuất -> về trang đăng nhập
        from pages.login import LoginPage

        self.trang_dang_nhap = LoginPage(main_window=self.cua_so_chinh, root_dir=self.thu_muc_goc)
        self.close()
