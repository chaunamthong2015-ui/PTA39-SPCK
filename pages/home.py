# ==========================================================
# home.py - Trang CHỦ (ui/home.ui)
# ==========================================================
# Hiển thị tất cả món hàng (đọc từ data/products.json)
# bằng VÒNG FOR: mỗi món hàng -> 1 TheSanPham -> bỏ vào lưới.

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import os

from entities.products import QuanLySanPham
from components.product_card import TheSanPham

SO_COT = 3  # số thẻ trên 1 hàng


class TrangChu(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan  # người dùng đang đăng nhập (object NguoiDung)

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "home.ui")
        uic.loadUi(duong_dan_ui, self)

        # bắt sự kiện cho các nút
        self.nut_tim_kiem.clicked.connect(self.chuyen_trang_tim_kiem)
        self.o_tim_kiem.returnPressed.connect(self.chuyen_trang_tim_kiem)  # nhấn Enter cũng tìm
        self.nut_gio_hang.clicked.connect(self.chuyen_trang_gio_hang)
        self.nut_tai_khoan.clicked.connect(self.chuyen_trang_tai_khoan)

        self.hien_thi_danh_sach_san_pham()
        self.show()

    # ------------------ xử lý sự kiện ------------------
    def hien_thi_danh_sach_san_pham(self):
        # lấy layout dạng lưới bên trong vùng cuộn
        luoi = self.danh_sach_san_pham.layout()

        # lấy danh sách món hàng từ file json
        danh_sach = QuanLySanPham().lay_tat_ca()

        # VÒNG FOR: tạo thẻ cho từng món rồi đặt vào lưới
        # enumerate cho biết thứ tự (vi_tri) của món: 0, 1, 2, ...
        for vi_tri, san_pham in enumerate(danh_sach):
            the = TheSanPham(thu_muc_goc=self.thu_muc_goc, san_pham=san_pham, tai_khoan=self.tai_khoan)
            hang = vi_tri // SO_COT  # chia lấy phần nguyên -> số hàng
            cot = vi_tri % SO_COT    # chia lấy phần dư    -> số cột
            luoi.addWidget(the, hang, cot)

    def chuyen_trang_tim_kiem(self):
        tu_khoa = self.o_tim_kiem.text().strip()
        if tu_khoa == "":
            self.hien_thong_bao("Vui lòng điền từ khóa để tìm kiếm!")
            return

        from pages.search import TrangTimKiem

        # lưu vào self để cửa sổ không bị tự đóng
        # KHÔNG close() -> trang chủ vẫn mở phía sau
        self.trang_tim_kiem = TrangTimKiem(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc,
            tai_khoan=self.tai_khoan, tu_khoa=tu_khoa,
        )

    def chuyen_trang_gio_hang(self):
        from pages.gio_hang import TrangGioHang

        self.trang_gio_hang = TrangGioHang(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    def chuyen_trang_tai_khoan(self):
        from pages.account import TrangTaiKhoan

        self.trang_tai_khoan = TrangTaiKhoan(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Information)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
