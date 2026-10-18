# ==========================================================
# gio_hang.py - Trang GIỎ HÀNG (ui/gio_hang.ui)
# ==========================================================
# Dùng VÒNG FOR: mỗi món trong giỏ -> 1 TheMonTrongGio.
# Tăng / giảm / xóa món -> lưu lại vào users.json.

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic
import os

from entities.users import QuanLyNguoiDung
from entities.products import QuanLySanPham
from entities.product import SanPham
from components.cart_item_card import TheMonTrongGio

PHI_VAN_CHUYEN = 30000  # phí ship cố định (đổi số này nếu muốn)


class TrangGioHang(QMainWindow):
    def __init__(self, cua_so_chinh, thu_muc_goc, tai_khoan):
        super().__init__()
        self.cua_so_chinh = cua_so_chinh
        self.thu_muc_goc = thu_muc_goc
        self.tai_khoan = tai_khoan
        self.quan_ly_san_pham = QuanLySanPham()

        duong_dan_ui = os.path.join(self.thu_muc_goc, "ui", "gio_hang.ui")
        uic.loadUi(duong_dan_ui, self)

        # bắt sự kiện cho các nút
        self.nut_trang_chu.clicked.connect(self.chuyen_trang_chu)
        self.nut_thanh_toan.clicked.connect(self.chuyen_trang_thanh_toan)
        self.nut_tim_kiem.clicked.connect(self.chuyen_trang_tim_kiem)
        self.o_tim_kiem.returnPressed.connect(self.chuyen_trang_tim_kiem)

        self.hien_thi_gio_hang()
        self.show()

    # ------------------ chức năng chính ------------------
    def hien_thi_gio_hang(self):
        bo_cuc = self.danh_sach_gio_hang.layout()

        # 1. xóa hết thẻ cũ (đi ngược từ cuối lên đầu)
        for vi_tri in reversed(range(bo_cuc.count())):
            phan_tu = bo_cuc.takeAt(vi_tri)
            if phan_tu.widget() is not None:
                phan_tu.widget().deleteLater()

        # 2. VÒNG FOR: mỗi món trong giỏ -> 1 thẻ
        for mon in self.tai_khoan.lay_gio_hang():
            san_pham = self.quan_ly_san_pham.tim_san_pham(mon["ma_san_pham"])
            if san_pham is None:
                continue  # món đã bị xóa khỏi cửa hàng -> bỏ qua
            the = TheMonTrongGio(
                thu_muc_goc=self.thu_muc_goc, san_pham=san_pham,
                so_luong=mon["so_luong"], trang_gio_hang=self,
            )
            bo_cuc.addWidget(the)

        bo_cuc.addStretch()  # đẩy các thẻ lên trên cùng

        # 3. cập nhật phần tổng kết bên phải
        self.cap_nhat_tong_ket()

    def tinh_tien_hang(self):
        # tổng tiền hàng = cộng (giá x số lượng) của từng món
        tong = 0
        for mon in self.tai_khoan.lay_gio_hang():
            san_pham = self.quan_ly_san_pham.tim_san_pham(mon["ma_san_pham"])
            if san_pham is not None:
                tong += san_pham.lay_gia() * mon["so_luong"]
        return tong

    def cap_nhat_tong_ket(self):
        so_mon = 0
        for mon in self.tai_khoan.lay_gio_hang():
            so_mon += mon["so_luong"]

        tien_hang = self.tinh_tien_hang()
        phi_ship = PHI_VAN_CHUYEN if so_mon > 0 else 0  # giỏ rỗng -> không tính ship

        self.so_luong_san_pham.setText(f"Number: {so_mon}")
        self.phi_van_chuyen.setText(f"Shipping: {SanPham.dinh_dang_tien(phi_ship)}")
        self.tong_tien.setText(f"Total: {SanPham.dinh_dang_tien(tien_hang + phi_ship)}")

    # 2 hàm dưới được TheMonTrongGio gọi khi bấm nút +, -, X
    def doi_so_luong(self, ma_san_pham, so_luong_moi):
        self.tai_khoan.doi_so_luong_mon(ma_san_pham, so_luong_moi)
        self.luu_va_ve_lai()

    def xoa_mon(self, ma_san_pham):
        self.tai_khoan.xoa_khoi_gio(ma_san_pham)
        self.luu_va_ve_lai()

    def luu_va_ve_lai(self):
        QuanLyNguoiDung().sua_nguoi_dung(self.tai_khoan)  # lưu giỏ hàng vào users.json
        self.hien_thi_gio_hang()                 # vẽ lại danh sách

    # ------------------ chuyển trang ------------------
    def chuyen_trang_chu(self):
        from pages.home import TrangChu

        self.trang_chu = TrangChu(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    def chuyen_trang_thanh_toan(self):
        if len(self.tai_khoan.lay_gio_hang()) == 0:
            self.hien_thong_bao("Giỏ hàng đang trống!")
            return

        from pages.checkout import TrangThanhToan

        self.trang_thanh_toan = TrangThanhToan(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc, tai_khoan=self.tai_khoan
        )
        self.close()

    def chuyen_trang_tim_kiem(self):
        tu_khoa = self.o_tim_kiem.text().strip()
        if tu_khoa == "":
            self.hien_thong_bao("Vui lòng điền từ khóa để tìm kiếm!")
            return

        from pages.search import TrangTimKiem

        self.trang_tim_kiem = TrangTimKiem(
            cua_so_chinh=self.cua_so_chinh, thu_muc_goc=self.thu_muc_goc,
            tai_khoan=self.tai_khoan, tu_khoa=tu_khoa,
        )

    # ------------------ hàm hỗ trợ ------------------
    def hien_thong_bao(self, noi_dung):
        hop_thoai = QMessageBox()
        hop_thoai.setWindowTitle("Thông báo")
        hop_thoai.setText(noi_dung)
        hop_thoai.setIcon(QMessageBox.Icon.Information)
        hop_thoai.setStandardButtons(QMessageBox.StandardButton.Ok)
        hop_thoai.exec()
