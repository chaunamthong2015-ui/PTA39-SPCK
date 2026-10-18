# ==========================================================
# details.py - Trang CHI TIẾT món hàng (ui/details.ui)
# ==========================================================
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import uic
import os

from entities.users import QuanLyNguoiDung


class TrangChiTiet(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan, san_pham):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan
        self.san_pham = san_pham  # 1 object SanPham

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "details.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()

        # nút ADD TO CART -> thêm vào giỏ hàng
        self.nut_them_gio_hang.clicked.connect(self.them_vao_gio_hang)

        self.show()

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_thong_tin(self):
        # ảnh: giữ đúng tỉ lệ (KeepAspectRatio), co giãn mượt (SmoothTransformation)
        duong_dan_anh = os.path.join(self.thu_muc_goc, self.san_pham.lay_hinh_anh())
        anh = QPixmap(duong_dan_anh)
        if not anh.isNull():
            anh_nho = anh.scaled(
                481, 301,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            self.hinh_anh.setPixmap(anh_nho)

        self.ten_san_pham.setText(self.san_pham.lay_ten())
        self.gia.setText(f"Giá: {self.san_pham.lay_gia_hien_thi()}")
        self.mo_ta.setText(self.san_pham.lay_mo_ta())
        self.nguoi_dang.setText(f"Bởi: {self.san_pham.lay_nguoi_dang()}")
        self.ngay_dang.setText(f"Ngày đăng bán: {self.san_pham.lay_ngay_dang()}")

        # tiêu đề cửa sổ = tên món hàng
        self.setWindowTitle(self.san_pham.lay_ten())

    def them_vao_gio_hang(self):
        if self.tai_khoan is None:
            self.hien_thong_bao("Bạn cần đăng nhập để mua hàng!")
            return

        # 1. thêm món vào giỏ của người dùng
        self.tai_khoan.them_vao_gio(self.san_pham.lay_ma())
        # 2. lưu người dùng (có giỏ hàng mới) vào users.json
        QuanLyNguoiDung().sua_nguoi_dung(self.tai_khoan)

        self.hien_thong_bao(f"Đã thêm '{self.san_pham.lay_ten()}' vào giỏ hàng!")

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Information)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
