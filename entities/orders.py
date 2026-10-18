# ==========================================================
# orders.py - Class QuanLyDonHang: quản lý DANH SÁCH đơn hàng
# ==========================================================
# Chức năng: lấy / tìm / thêm / xóa
# Dữ liệu lưu trong data/orders.json

import os
from data.data_io import DataIO
from entities.order import DonHang

THU_MUC_GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DON_HANG = os.path.join(THU_MUC_GOC, "data", "orders.json")


class QuanLyDonHang:
    def __init__(self):
        self.__danh_sach_don_hang = []  # list chứa các object DonHang
        self.doc_file()

    # ------------------ ĐỌC / GHI FILE JSON ------------------
    def doc_file(self):
        if not os.path.exists(FILE_DON_HANG):
            self.__danh_sach_don_hang = []
            return
        danh_sach_dict = DataIO.read_json(FILE_DON_HANG)
        self.__danh_sach_don_hang = []
        for du_lieu in danh_sach_dict:
            self.__danh_sach_don_hang.append(DonHang.tao_tu_dict(du_lieu))

    def luu_file(self):
        danh_sach_dict = []
        for don_hang in self.__danh_sach_don_hang:
            danh_sach_dict.append(don_hang.chuyen_thanh_dict())
        DataIO.write_json(FILE_DON_HANG, danh_sach_dict)

    # ------------------ LẤY / TÌM ------------------
    def lay_tat_ca(self):
        return self.__danh_sach_don_hang

    def tim_don_hang(self, ma_don_hang_can_tim):
        for don_hang in self.__danh_sach_don_hang:
            if don_hang.lay_ma() == ma_don_hang_can_tim:
                return don_hang
        return None

    # Lấy các đơn hàng của 1 tài khoản
    def lay_don_hang_theo_email(self, email):
        ket_qua = []
        for don_hang in self.__danh_sach_don_hang:
            if don_hang.lay_email_tai_khoan() == email:
                ket_qua.append(don_hang)
        return ket_qua

    # Mã đơn mới = mã lớn nhất + 1
    def tao_ma_moi(self):
        ma_lon_nhat = 0
        for don_hang in self.__danh_sach_don_hang:
            if don_hang.lay_ma() > ma_lon_nhat:
                ma_lon_nhat = don_hang.lay_ma()
        return ma_lon_nhat + 1

    # ------------------ THÊM ------------------
    def them_don_hang(self, don_hang_moi):
        self.__danh_sach_don_hang.append(don_hang_moi)
        self.luu_file()

    # ------------------ XÓA ------------------
    def xoa_don_hang(self, ma_don_hang_can_tim):
        don_hang = self.tim_don_hang(ma_don_hang_can_tim)
        if don_hang is None:
            return False
        self.__danh_sach_don_hang.remove(don_hang)
        self.luu_file()
        return True
