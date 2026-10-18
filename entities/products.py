# ==========================================================
# products.py - Class QuanLySanPham: quản lý DANH SÁCH món hàng
# ==========================================================
# Chức năng: lấy / tìm / thêm / sửa / xóa
# Dữ liệu lưu trong data/products.json

import os
from data.data_io import DataIO
from entities.product import SanPham

THU_MUC_GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_SAN_PHAM = os.path.join(THU_MUC_GOC, "data", "products.json")


class QuanLySanPham:
    def __init__(self):
        self.__danh_sach_san_pham = []  # list chứa các object SanPham
        self.doc_file()

    # ------------------ ĐỌC / GHI FILE JSON ------------------
    def doc_file(self):
        if not os.path.exists(FILE_SAN_PHAM):
            self.__danh_sach_san_pham = []
            return
        danh_sach_dict = DataIO.read_json(FILE_SAN_PHAM)
        self.__danh_sach_san_pham = []
        for du_lieu in danh_sach_dict:
            self.__danh_sach_san_pham.append(SanPham.tao_tu_dict(du_lieu))

    def luu_file(self):
        danh_sach_dict = []
        for san_pham in self.__danh_sach_san_pham:
            danh_sach_dict.append(san_pham.chuyen_thanh_dict())
        DataIO.write_json(FILE_SAN_PHAM, danh_sach_dict)

    # ------------------ LẤY / TÌM ------------------
    def lay_tat_ca(self):
        return self.__danh_sach_san_pham

    def tim_san_pham(self, ma_san_pham):
        for san_pham in self.__danh_sach_san_pham:
            if san_pham.lay_ma() == ma_san_pham:
                return san_pham
        return None

    # Tìm theo tên hoặc mô tả (không phân biệt chữ hoa / thường)
    def tim_kiem(self, tu_khoa):
        tu_khoa = tu_khoa.lower()
        ket_qua = []
        for san_pham in self.__danh_sach_san_pham:
            if tu_khoa in san_pham.lay_ten().lower() or tu_khoa in san_pham.lay_mo_ta().lower():
                ket_qua.append(san_pham)
        return ket_qua

    # ------------------ THÊM ------------------
    def them_san_pham(self, san_pham_moi):
        if self.tim_san_pham(san_pham_moi.lay_ma()) is not None:
            return False  # trùng mã -> không thêm
        self.__danh_sach_san_pham.append(san_pham_moi)
        self.luu_file()
        return True

    # Tạo mã mới = mã lớn nhất + 1 (dùng khi thêm món hàng mới)
    def tao_ma_moi(self):
        ma_lon_nhat = 0
        for san_pham in self.__danh_sach_san_pham:
            if san_pham.lay_ma() > ma_lon_nhat:
                ma_lon_nhat = san_pham.lay_ma()
        return ma_lon_nhat + 1

    # ------------------ SỬA ------------------
    def sua_san_pham(self, san_pham_da_sua):
        for vi_tri in range(len(self.__danh_sach_san_pham)):
            if self.__danh_sach_san_pham[vi_tri].lay_ma() == san_pham_da_sua.lay_ma():
                self.__danh_sach_san_pham[vi_tri] = san_pham_da_sua
                self.luu_file()
                return True
        return False

    # ------------------ XÓA ------------------
    def xoa_san_pham(self, ma_san_pham):
        san_pham = self.tim_san_pham(ma_san_pham)
        if san_pham is None:
            return False
        self.__danh_sach_san_pham.remove(san_pham)
        self.luu_file()
        return True
