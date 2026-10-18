# ==========================================================
# order_card.py - Thẻ (card) hiển thị MỘT đơn hàng (trang lịch sử)
# ==========================================================
# Giao diện thẻ: ui/order_card.ui

import os
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from entities.product import SanPham


class TheDonHang(QWidget):
    def __init__(self, thu_muc_goc, don_hang):
        super().__init__()
        self.thu_muc_goc = thu_muc_goc
        self.don_hang = don_hang  # 1 object DonHang

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "order_card.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_thong_tin()

    def hien_thi_thong_tin(self):
        self.ma_don_hang.setText(f"Đơn hàng #{self.don_hang.lay_ma()}")
        self.ngay_dat.setText(f"Ngày đặt: {self.don_hang.lay_ngay_dat()}")

        # Ghép tên các món thành 1 dòng, ví dụ: "Rubik 3x3 x2, Diều giấy mini x1"
        cac_mon = []
        for mon in self.don_hang.lay_danh_sach_mon():
            cac_mon.append(f"{mon['ten']} x{mon['so_luong']}")
        self.danh_sach_mon.setText("Món hàng: " + ", ".join(cac_mon))

        tong = SanPham.dinh_dang_tien(self.don_hang.lay_tong_tien())
        self.tong_tien.setText(f"Tổng tiền: {tong}")
