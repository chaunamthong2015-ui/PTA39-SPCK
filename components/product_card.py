# ==========================================================
# product_card.py - Thẻ (card) hiển thị MỘT món hàng
# ==========================================================
# Giao diện thẻ: ui/product_card.ui
# Trang chủ và trang tìm kiếm dùng vòng for để tạo nhiều thẻ.

import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap  # dùng để hiện ảnh trong QLabel
from PyQt6 import uic


class TheSanPham(QWidget):
    def __init__(self, thu_muc_goc, san_pham, tai_khoan):
        super().__init__()
        self.thu_muc_goc = thu_muc_goc
        self.san_pham = san_pham  # 1 object SanPham
        self.tai_khoan = tai_khoan    # tài khoản đang đăng nhập (object NguoiDung)

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "product_card.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()

        # bấm nút -> mở trang chi tiết
        self.nut_chi_tiet.clicked.connect(self.chuyen_trang_chi_tiet)

        # KHÔNG gọi self.show() vì thẻ nằm bên trong trang khác

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_thong_tin(self):
        # 1. Ảnh: ghép thư mục gốc + đường dẫn ảnh trong json
        duong_dan_anh = os.path.join(self.thu_muc_goc, self.san_pham.lay_hinh_anh())
        anh = QPixmap(duong_dan_anh)
        if anh.isNull():
            print(f"[CẢNH BÁO] Không tìm thấy ảnh: {duong_dan_anh}")
        else:
            self.hinh_anh.setPixmap(anh.scaled(200, 200))

        # 2. Tên và giá
        self.ten_san_pham.setText(self.san_pham.lay_ten())
        self.gia.setText(self.san_pham.lay_gia_hien_thi())

    def chuyen_trang_chi_tiet(self):
        from pages.details import TrangChiTiet

        # lưu vào self để cửa sổ không bị tự đóng
        self.trang_chi_tiet = TrangChiTiet(
            cua_so_chinh=None,
            thu_muc_goc=self.thu_muc_goc,
            tai_khoan=self.tai_khoan,
            san_pham=self.san_pham,
        )
