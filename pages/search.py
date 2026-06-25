import random
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem

# QListWidgetItem: đại diện cho 1 dòng trong QListWidget
# Mỗi item trong list sẽ là 1 object QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6 import uic

# ✅ Import danh sách món hàng từ home để tìm kiếm trên đó
# Tránh tạo lại data ở nhiều nơi — chỉ có 1 nguồn duy nhất (Single Source of Truth)
from pages.home import danhsach_monhang


class SearchPage(QMainWindow):
    def __init__(self, main_window, root_dir, search_key):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.search_key = search_key

        # ✅ Lưu danh sách kết quả tìm được để dùng khi click item
        # Ban đầu là rỗng, sẽ được gán trong set_search_list()
        self.ket_qua = []

        ui_path = self.root_dir + "/ui/search.ui"
        uic.loadUi(ui_path, self)

        # ✅ Gắn sự kiện: khi double-click vào 1 dòng trong list → chuyển trang detail
        # itemDoubleClicked: signal phát ra khi người dùng double-click vào 1 item
        # Single click dùng itemClicked nếu muốn
        self.search_list.itemDoubleClicked.connect(self.goto_details)

        # Điền nội dung
        self.set_search_list()  # phải chạy trước để có self.ket_qua
        self.set_result_title()  # chạy sau để biết tìm được bao nhiêu cái

        self.show()

    # ------------------ xử lý sự kiện ------------------
    def set_result_title(self):
        so_ket_qua = len(self.ket_qua)
        result = f"Kết quả tìm kiếm cho '{self.search_key}' ({so_ket_qua})"
        self.result_title.setText(result)

    def set_search_list(self):
        # ✅ Bước 1: Lọc danh sách món hàng theo từ khóa (không phân biệt hoa/thường)
        # .lower(): chuyển chuỗi về chữ thường để so sánh không phân biệt hoa/thường
        # Ví dụ: "Bánh" và "bánh" đều khớp với từ khóa "bánh"
        tu_khoa = self.search_key.lower()

        self.ket_qua = [
            mon
            for mon in danhsach_monhang
            # ✅ Tìm trong name VÀ details — dùng OR (or) để khớp cả hai trường
            if tu_khoa in mon["name"].lower() or tu_khoa in mon["details"].lower()
        ]
        # Cú pháp trên gọi là "list comprehension":
        # [phần_tử for phần_tử in danh_sách if điều_kiện]
        # Kết quả: danh sách mới chỉ gồm các món thỏa điều kiện

        # ✅ Bước 2: Xóa list cũ (nếu gọi lại hàm này nhiều lần không bị duplicate)
        self.search_list.clear()

        if len(self.ket_qua) == 0:
            # Không có kết quả → thêm 1 dòng thông báo không thể click
            khong_co = QListWidgetItem("Không tìm thấy sản phẩm nào.")
            # Qt.ItemFlag.NoItemFlags: tắt hết tương tác (không click, không chọn được)
            khong_co.setFlags(Qt.ItemFlag.NoItemFlags)
            self.search_list.addItem(khong_co)
            return  # dừng sớm, không chạy code phía dưới nữa

        # ✅ Bước 3: Thêm từng kết quả vào QListWidget
        for mon in self.ket_qua:
            # Nội dung hiển thị: "Tên món — Giá"
            noi_dung = f"{mon['name']}  —  {mon['price']}"

            # Tạo 1 dòng trong list
            item = QListWidgetItem(noi_dung)

            # ✅ Gắn toàn bộ dict món hàng vào item để dùng lại khi click
            # setData(role, value): lưu dữ liệu vào item theo "vai trò" (role)
            # Qt.ItemDataRole.UserRole: slot dành riêng cho developer lưu data tùy ý
            # → Khi click item, ta lấy lại bằng item.data(Qt.ItemDataRole.UserRole)
            item.setData(Qt.ItemDataRole.UserRole, mon)

            self.search_list.addItem(item)

    def goto_details(self, item):
        # ✅ item là QListWidgetItem mà người dùng vừa double-click
        # Lấy lại dict món hàng đã lưu lúc trước
        mon_hang = item.data(Qt.ItemDataRole.UserRole)

        # Random ảnh 1 hoặc 2 (giống logic ở home)
        so_anh = random.choice([1, 2])
        img_path = f"{self.root_dir}/assets/imgs/image_{so_anh}.jpg"
        mon_hang_voi_anh = {**mon_hang, "img": img_path}

        from pages.details import DetailsPage

        # Mở trang chi tiết
        self.details_page = DetailsPage(
            main_window=self.main_window,
            root_dir=self.root_dir,
            cur_acc=None,  # TODO: truyền cur_acc vào SearchPage nếu cần
            product_data=mon_hang_voi_anh,
        )

        # ✅ Đóng cửa sổ Search, Home vẫn còn vì chưa gọi close() trên Home
        self.close()

    # ------------------ hàm hỗ trợ ------------------
    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
