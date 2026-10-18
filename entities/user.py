# ==========================================================
# user.py - Class NguoiDung: lưu thông tin MỘT người dùng
# ==========================================================
# Mỗi NguoiDung gồm:
#   - ho_ten   : họ tên
#   - email    : email (dùng để đăng nhập, không được trùng)
#   - mat_khau : mật khẩu
#   - gio_hang : giỏ hàng, là 1 list, mỗi phần tử có dạng
#                {"ma_san_pham": 1, "so_luong": 2}


class NguoiDung:
    def __init__(self, ho_ten, email, mat_khau, gio_hang=None):
        # dấu __ ở đầu: thuộc tính "riêng tư", chỉ đọc/sửa qua hàm lay_... / sua_...
        self.__ho_ten = ho_ten
        self.__email = email
        self.__mat_khau = mat_khau

        # chưa có giỏ hàng -> tạo giỏ hàng rỗng
        if gio_hang is None:
            gio_hang = []
        self.__gio_hang = gio_hang

    def __str__(self):
        return f"NguoiDung(ho_ten={self.__ho_ten}, email={self.__email})"

    # ------------------ HÀM LẤY (lay_...) ------------------
    def lay_ho_ten(self):
        return self.__ho_ten

    def lay_email(self):
        return self.__email

    def lay_mat_khau(self):
        return self.__mat_khau

    def lay_gio_hang(self):
        return self.__gio_hang

    # ------------------ HÀM SỬA (sua_..., có kiểm tra) ------------------
    def sua_ho_ten(self, ho_ten):
        if ho_ten.strip() != "":
            self.__ho_ten = ho_ten
        else:
            print("Họ tên không được để trống!")

    def sua_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Email không hợp lệ!")

    def sua_mat_khau(self, mat_khau):
        if len(mat_khau) >= 6:
            self.__mat_khau = mat_khau
        else:
            print("Mật khẩu phải từ 6 ký tự trở lên!")

    # ------------------ GIỎ HÀNG ------------------
    def them_vao_gio(self, ma_san_pham):
        # Đã có trong giỏ -> tăng số lượng thêm 1
        for mon in self.__gio_hang:
            if mon["ma_san_pham"] == ma_san_pham:
                mon["so_luong"] += 1
                return
        # Chưa có -> thêm mới với số lượng 1
        self.__gio_hang.append({"ma_san_pham": ma_san_pham, "so_luong": 1})

    def doi_so_luong_mon(self, ma_san_pham, so_luong_moi):
        # Số lượng về 0 -> bỏ món đó khỏi giỏ
        if so_luong_moi <= 0:
            self.xoa_khoi_gio(ma_san_pham)
            return
        for mon in self.__gio_hang:
            if mon["ma_san_pham"] == ma_san_pham:
                mon["so_luong"] = so_luong_moi

    def xoa_khoi_gio(self, ma_san_pham):
        # Giữ lại những món KHÁC mã cần xóa
        self.__gio_hang = [
            mon for mon in self.__gio_hang if mon["ma_san_pham"] != ma_san_pham
        ]

    def xoa_het_gio(self):
        self.__gio_hang = []

    # ------------------ CHUYỂN ĐỔI object <-> dict ------------------
    # object -> dict (để lưu vào file json)
    def chuyen_thanh_dict(self):
        return {
            "ho_ten": self.__ho_ten,
            "email": self.__email,
            "mat_khau": self.__mat_khau,
            "gio_hang": self.__gio_hang,
        }

    # dict -> object (khi đọc từ file json)
    @classmethod
    def tao_tu_dict(cls, du_lieu):
        return cls(
            ho_ten=du_lieu.get("ho_ten", ""),
            email=du_lieu.get("email", ""),
            mat_khau=du_lieu.get("mat_khau", ""),
            gio_hang=du_lieu.get("gio_hang", []),
        )
