# ==========================================================
# lich_su.py - Trang LỊCH SỬ MUA HÀNG (ui/lich_su.ui)
# ==========================================================
# Dùng VÒNG FOR: mỗi đơn hàng -> 1 TheDonHang -> bỏ vào list.

from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic
import os

from entities.orders import QuanLyDonHang
from components.order_card import TheDonHang


class TrangLichSu(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "lich_su.ui")
        uic.loadUi(duong_dan_ui, self)

        self.nut_tai_khoan.clicked.connect(self.chuyen_trang_tai_khoan)

        self.hien_thi_lich_su()
        self.show()

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_lich_su(self):
        # chỉ lấy đơn hàng của tài khoản đang đăng nhập
        danh_sach = QuanLyDonHang().lay_don_hang_theo_email(self.tai_khoan.lay_email())

        self.danh_sach_don_hang.clear()
        if len(danh_sach) == 0:
            self.danh_sach_don_hang.addItem("Bạn chưa có đơn hàng nào.")
            return

        # reversed: đơn mới nhất hiện lên đầu
        for don_hang in reversed(danh_sach):
            the = TheDonHang(thu_muc_goc=self.thu_muc_goc, don_hang=don_hang)
            dong = QListWidgetItem()
            dong.setSizeHint(the.sizeHint())
            self.danh_sach_don_hang.addItem(dong)
            self.danh_sach_don_hang.setItemWidget(dong, the)

    def chuyen_trang_tai_khoan(self):
        from pages.account import TrangTaiKhoan

        self.trang_tai_khoan = TrangTaiKhoan(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()
