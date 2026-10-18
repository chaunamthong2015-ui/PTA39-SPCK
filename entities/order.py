# ==========================================================
# order.py - Class DonHang: lưu thông tin MỘT đơn hàng
# ==========================================================
# Tạo ra khi người dùng bấm PLACE ORDER ở trang checkout.
# Các thuộc tính lấy theo form checkout.ui + giỏ hàng.


class DonHang:
    def __init__(self, ma, email_tai_khoan, ho_ten, email, dia_chi, thanh_pho,
                 ma_buu_dien, danh_sach_mon, phi_van_chuyen, tong_tien, ngay_dat):
        self.__ma = ma                          # mã đơn hàng
        self.__email_tai_khoan = email_tai_khoan  # tài khoản đã đặt đơn
        self.__ho_ten = ho_ten                  # tên người nhận
        self.__email = email                    # email người nhận
        self.__dia_chi = dia_chi                # địa chỉ giao hàng
        self.__thanh_pho = thanh_pho            # thành phố
        self.__ma_buu_dien = ma_buu_dien        # mã bưu điện
        # danh_sach_mon: list dict {"ma_san_pham", "ten", "gia", "so_luong"}
        self.__danh_sach_mon = danh_sach_mon
        self.__phi_van_chuyen = phi_van_chuyen  # phí ship
        self.__tong_tien = tong_tien            # tổng tiền (đã cộng ship)
        self.__ngay_dat = ngay_dat              # ngày đặt, ví dụ "14/10/2026"

    def __str__(self):
        return f"DonHang(ma={self.__ma}, tong_tien={self.__tong_tien})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ma(self):
        return self.__ma

    def lay_email_tai_khoan(self):
        return self.__email_tai_khoan

    def lay_ho_ten(self):
        return self.__ho_ten

    def lay_email(self):
        return self.__email

    def lay_dia_chi(self):
        return self.__dia_chi

    def lay_thanh_pho(self):
        return self.__thanh_pho

    def lay_ma_buu_dien(self):
        return self.__ma_buu_dien

    def lay_danh_sach_mon(self):
        return self.__danh_sach_mon

    def lay_phi_van_chuyen(self):
        return self.__phi_van_chuyen

    def lay_tong_tien(self):
        return self.__tong_tien

    def lay_ngay_dat(self):
        return self.__ngay_dat

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    def chuyen_thanh_dict(self):
        return {
            "ma": self.__ma,
            "email_tai_khoan": self.__email_tai_khoan,
            "ho_ten": self.__ho_ten,
            "email": self.__email,
            "dia_chi": self.__dia_chi,
            "thanh_pho": self.__thanh_pho,
            "ma_buu_dien": self.__ma_buu_dien,
            "danh_sach_mon": self.__danh_sach_mon,
            "phi_van_chuyen": self.__phi_van_chuyen,
            "tong_tien": self.__tong_tien,
            "ngay_dat": self.__ngay_dat,
        }

    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ma=du_lieu.get("ma"),
            email_tai_khoan=du_lieu.get("email_tai_khoan", ""),
            ho_ten=du_lieu.get("ho_ten", ""),
            email=du_lieu.get("email", ""),
            dia_chi=du_lieu.get("dia_chi", ""),
            thanh_pho=du_lieu.get("thanh_pho", ""),
            ma_buu_dien=du_lieu.get("ma_buu_dien", ""),
            danh_sach_mon=du_lieu.get("danh_sach_mon", []),
            phi_van_chuyen=du_lieu.get("phi_van_chuyen", 0),
            tong_tien=du_lieu.get("tong_tien", 0),
            ngay_dat=du_lieu.get("ngay_dat", ""),
        )
