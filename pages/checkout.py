# ==========================================================
# checkout.py - Trang THANH TOÁN (ui/checkout.ui)
# ==========================================================
# Điền thông tin giao hàng -> PLACE ORDER -> lưu đơn vào orders.json

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
from datetime import date
import os
import re

from entities.users import QuanLyNguoiDung
from entities.products import QuanLySanPham
from entities.product import SanPham
from entities.order import DonHang
from entities.orders import QuanLyDonHang
from pages.gio_hang import PHI_VAN_CHUYEN


class TrangThanhToan(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "checkout.ui")
        uic.loadUi(duong_dan_ui, self)

        # điền sẵn tên + email của tài khoản cho nhanh
        self.o_ho_ten.setText(self.tai_khoan.lay_ho_ten())
        self.o_email.setText(self.tai_khoan.lay_email())

        # tính tiền từ giỏ hàng và hiện lên
        self.danh_sach_mon = self.lay_danh_sach_mon()
        self.tong_tien_don = self.tinh_tong_tien()
        self.tong_tien.setText(f"Total: {SanPham.dinh_dang_tien(self.tong_tien_don)}")

        # bắt sự kiện cho các nút
        self.nut_dat_hang.clicked.connect(self.dat_hang)
        self.nut_quay_lai.clicked.connect(self.chuyen_trang_gio_hang)

        self.show()

    # ------------------ chức năng chính ------------------
    def lay_danh_sach_mon(self):
        # chép thông tin món (tên, giá) vào đơn hàng,
        # để sau này món có đổi giá thì đơn cũ vẫn đúng
        quan_ly_san_pham = QuanLySanPham()
        danh_sach = []
        for mon in self.tai_khoan.lay_gio_hang():
            san_pham = quan_ly_san_pham.tim_san_pham(mon["ma_san_pham"])
            if san_pham is not None:
                danh_sach.append({
                    "ma_san_pham": san_pham.lay_ma(),
                    "ten": san_pham.lay_ten(),
                    "gia": san_pham.lay_gia(),
                    "so_luong": mon["so_luong"],
                })
        return danh_sach

    def tinh_tong_tien(self):
        tong = PHI_VAN_CHUYEN
        for mon in self.danh_sach_mon:
            tong += mon["gia"] * mon["so_luong"]
        return tong

    def kiem_tra_form(self):
        # kiểm tra form, có lỗi -> trả về câu báo lỗi
        if self.o_ho_ten.text().strip() == "":
            return "Vui lòng nhập họ tên người nhận!"

        mau_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.fullmatch(mau_email, self.o_email.text().strip()) is None:
            return "Email không hợp lệ!"

        # QTextEdit dùng toPlainText() thay cho text()
        if self.o_dia_chi.toPlainText().strip() == "":
            return "Vui lòng nhập địa chỉ giao hàng!"

        if self.o_thanh_pho.text().strip() == "":
            return "Vui lòng nhập thành phố!"

        # isdigit(): chỉ toàn chữ số
        if not self.o_ma_buu_dien.text().strip().isdigit():
            return "Mã bưu điện chỉ gồm chữ số!"

        return None  # không có lỗi

    def dat_hang(self):
        loi = self.kiem_tra_form()
        if loi is not None:
            self.hien_thong_bao(loi)
            return

        # 1. tạo đơn hàng mới
        quan_ly_don_hang = QuanLyDonHang()
        don_hang = DonHang(
            ma=quan_ly_don_hang.tao_ma_moi(),
            email_tai_khoan=self.tai_khoan.lay_email(),
            ho_ten=self.o_ho_ten.text().strip(),
            email=self.o_email.text().strip(),
            dia_chi=self.o_dia_chi.toPlainText().strip(),
            thanh_pho=self.o_thanh_pho.text().strip(),
            ma_buu_dien=self.o_ma_buu_dien.text().strip(),
            danh_sach_mon=self.danh_sach_mon,
            phi_van_chuyen=PHI_VAN_CHUYEN,
            tong_tien=self.tong_tien_don,
            ngay_dat=date.today().strftime("%d/%m/%Y"),  # ngày hôm nay
        )
        # 2. lưu đơn vào orders.json
        quan_ly_don_hang.them_don_hang(don_hang)

        # 3. đặt xong -> làm trống giỏ hàng + lưu người dùng
        self.tai_khoan.xoa_het_gio()
        QuanLyNguoiDung().sua_nguoi_dung(self.tai_khoan)

        self.hien_thong_bao("Đặt hàng thành công!")
        self.chuyen_trang_lich_su()

    # ------------------ chuyển trang ------------------
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

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Information)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
