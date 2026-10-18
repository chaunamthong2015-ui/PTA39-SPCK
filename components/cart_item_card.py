# ==========================================================
# cart_item_card.py - Thẻ (card) hiển thị MỘT món trong giỏ hàng
# ==========================================================
# Giao diện thẻ: ui/cart_item_card.ui
# Có 3 nút: - (giảm), + (tăng), X (xóa khỏi giỏ)

import os
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import uic


class TheMonTrongGio(QWidget):
    def __init__(self, thu_muc_goc, san_pham, so_luong, trang_gio_hang):
        super().__init__()
        self.thu_muc_goc = thu_muc_goc
        self.san_pham = san_pham              # 1 object SanPham
        self.so_luong_mon = so_luong          # số lượng trong giỏ
        self.trang_gio_hang = trang_gio_hang  # trang giỏ hàng (để báo khi bấm nút)

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "cart_item_card.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()

        # Bấm nút -> nhờ trang giỏ hàng xử lý (vì trang đó giữ dữ liệu)
        self.nut_cong.clicked.connect(self.bam_cong)
        self.nut_tru.clicked.connect(self.bam_tru)
        self.nut_xoa.clicked.connect(self.bam_xoa)

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_thong_tin(self):
        duong_dan_anh = os.path.join(self.thu_muc_goc, self.san_pham.lay_hinh_anh())
        anh = QPixmap(duong_dan_anh)
        if not anh.isNull():
            self.hinh_anh.setPixmap(anh)

        self.ten_san_pham.setText(self.san_pham.lay_ten())
        self.gia.setText(self.san_pham.lay_gia_hien_thi())
        self.so_luong.setText(str(self.so_luong_mon))

    def bam_cong(self):
        self.trang_gio_hang.doi_so_luong(self.san_pham.lay_ma(), self.so_luong_mon + 1)

    def bam_tru(self):
        self.trang_gio_hang.doi_so_luong(self.san_pham.lay_ma(), self.so_luong_mon - 1)

    def bam_xoa(self):
        self.trang_gio_hang.xoa_mon(self.san_pham.lay_ma())
