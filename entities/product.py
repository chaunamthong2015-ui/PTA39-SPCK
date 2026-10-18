# ==========================================================
# product.py - Class SanPham: lưu thông tin MỘT món hàng
# ==========================================================
# Các thuộc tính lấy theo những gì thẻ / trang chi tiết hiển thị:
#   ma, ten, gia, nguoi_dang, mo_ta, ngay_dang, hinh_anh


class SanPham:
    def __init__(self, ma, ten, gia, nguoi_dang, mo_ta, ngay_dang, hinh_anh):
        self.__ma = ma                  # mã món hàng (số, không trùng)
        self.__ten = ten                # tên món hàng
        self.__gia = gia                # giá (số nguyên), ví dụ 20000
        self.__nguoi_dang = nguoi_dang  # người đăng bán
        self.__mo_ta = mo_ta            # mô tả món hàng
        self.__ngay_dang = ngay_dang    # ngày đăng, ví dụ "21/06/2026"
        self.__hinh_anh = hinh_anh      # đường dẫn ảnh, ví dụ "assets/imgs/image_1.jpg"

    def __str__(self):
        return f"SanPham(ma={self.__ma}, ten={self.__ten}, gia={self.__gia})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ma(self):
        return self.__ma

    def lay_ten(self):
        return self.__ten

    def lay_gia(self):
        return self.__gia

    def lay_nguoi_dang(self):
        return self.__nguoi_dang

    def lay_mo_ta(self):
        return self.__mo_ta

    def lay_ngay_dang(self):
        return self.__ngay_dang

    def lay_hinh_anh(self):
        return self.__hinh_anh

    # Giá dạng chữ để hiển thị, ví dụ 20000 -> "20.000đ"
    def lay_gia_hien_thi(self):
        return SanPham.dinh_dang_tien(self.__gia)

    # ------------------ HÀM SỬA (sua_...) ------------------
    def sua_ten(self, ten):
        if ten.strip() != "":
            self.__ten = ten

    def sua_gia(self, gia):
        if gia >= 0:
            self.__gia = gia

    def sua_mo_ta(self, mo_ta):
        self.__mo_ta = mo_ta

    def sua_hinh_anh(self, hinh_anh):
        self.__hinh_anh = hinh_anh

    # ------------------ HÀM TIỆN ÍCH ------------------
    # staticmethod: gọi được luôn bằng SanPham.dinh_dang_tien(...)
    @staticmethod
    def dinh_dang_tien(so_tien):
        # f"{20000:,}" -> "20,000" rồi đổi dấu , thành dấu .
        return f"{so_tien:,}".replace(",", ".") + "đ"

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    def chuyen_thanh_dict(self):
        return {
            "ma": self.__ma,
            "ten": self.__ten,
            "gia": self.__gia,
            "nguoi_dang": self.__nguoi_dang,
            "mo_ta": self.__mo_ta,
            "ngay_dang": self.__ngay_dang,
            "hinh_anh": self.__hinh_anh,
        }

    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ma=du_lieu.get("ma"),
            ten=du_lieu.get("ten", ""),
            gia=du_lieu.get("gia", 0),
            nguoi_dang=du_lieu.get("nguoi_dang", ""),
            mo_ta=du_lieu.get("mo_ta", ""),
            ngay_dang=du_lieu.get("ngay_dang", ""),
            hinh_anh=du_lieu.get("hinh_anh", ""),
        )
