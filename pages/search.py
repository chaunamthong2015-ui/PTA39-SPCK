# ==========================================================
# search.py - Trang KẾT QUẢ TÌM KIẾM (ui/search.ui)
# ==========================================================
# Tìm món hàng theo tên / mô tả, rồi dùng VÒNG FOR
# bỏ từng TheSanPham vào danh sách (QListWidget).

from PyQt6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from PyQt6 import uic
import os

from entities.products import QuanLySanPham
from components.product_card import TheSanPham


class TrangTimKiem(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan, tu_khoa):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan
        self.tu_khoa = tu_khoa
        self.ket_qua = []  # các món tìm được

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "search.ui")
        uic.loadUi(duong_dan_ui, self)

        self.hien_thi_ket_qua()   # chạy trước để có self.ket_qua
        self.hien_thi_tieu_de()  # chạy sau để biết tìm được bao nhiêu món

        self.show()

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_tieu_de(self):
        so_ket_qua = len(self.ket_qua)
        self.tieu_de_ket_qua.setText(f"Kết quả tìm kiếm cho '{self.tu_khoa}' ({so_ket_qua})")

    def hien_thi_ket_qua(self):
        # 1. tìm trong file json
        self.ket_qua = QuanLySanPham().tim_kiem(self.tu_khoa)

        # 2. xóa danh sách cũ
        self.danh_sach_ket_qua.clear()

        if len(self.ket_qua) == 0:
            self.danh_sach_ket_qua.addItem("Không tìm thấy sản phẩm nào.")
            return

        # 3. VÒNG FOR: mỗi món -> 1 thẻ -> bỏ vào list
        for san_pham in self.ket_qua:
            the = TheSanPham(thu_muc_goc=self.thu_muc_goc, san_pham=san_pham, tai_khoan=self.tai_khoan)
            dong = QListWidgetItem()             # tạo 1 dòng trống
            dong.setSizeHint(the.sizeHint())    # dòng cao bằng thẻ
            self.danh_sach_ket_qua.addItem(dong)
            self.danh_sach_ket_qua.setItemWidget(dong, the)  # đặt thẻ vào dòng

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Information)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
