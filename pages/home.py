from datetime import date
import random  # ← dùng để random số 1 hoặc 2

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

# ✅ Danh sách 10 món hàng
# img để là placeholder "1" hoặc "2" — sẽ random khi tạo card
danhsach_monhang = [
    {
        "id": 1,
        "name": "Bánh tròn màu sắc",
        "price": "20.000đ",
        "created_by": "Nam Thông",
        "details": "Đồ chơi bằng nhựa PP nguyên sinh an toàn cho trẻ nhỏ, nhiều màu sắc.",
        "created_at": date(2026, 6, 21),
    },
    {
        "id": 2,
        "name": "Xe đồ chơi mini",
        "price": "35.000đ",
        "created_by": "Minh Anh",
        "details": "Xe mô hình nhỏ bằng hợp kim, sơn màu bền đẹp.",
        "created_at": date(2026, 6, 20),
    },
    {
        "id": 3,
        "name": "Búp bê vải",
        "price": "50.000đ",
        "created_by": "Thu Hà",
        "details": "Búp bê may bằng vải cotton mềm mại, an toàn cho bé.",
        "created_at": date(2026, 6, 19),
    },
    {
        "id": 4,
        "name": "Xếp hình gỗ",
        "price": "45.000đ",
        "created_by": "Quốc Bảo",
        "details": "Bộ xếp hình bằng gỗ tự nhiên, giúp phát triển tư duy.",
        "created_at": date(2026, 6, 18),
    },
    {
        "id": 5,
        "name": "Bóng cao su",
        "price": "15.000đ",
        "created_by": "Lan Nhi",
        "details": "Bóng cao su nhiều màu, đàn hồi tốt, an toàn.",
        "created_at": date(2026, 6, 17),
    },
    {
        "id": 6,
        "name": "Đất nặn màu",
        "price": "25.000đ",
        "created_by": "Hùng Cường",
        "details": "Đất nặn an toàn không độc hại, bộ 12 màu.",
        "created_at": date(2026, 6, 16),
    },
    {
        "id": 7,
        "name": "Tranh tô màu",
        "price": "18.000đ",
        "created_by": "Diệu Linh",
        "details": "Tập tranh tô màu chủ đề động vật, 20 trang.",
        "created_at": date(2026, 6, 15),
    },
    {
        "id": 8,
        "name": "Trống lắc tay",
        "price": "30.000đ",
        "created_by": "Phúc An",
        "details": "Trống lắc nhỏ bằng gỗ, âm thanh vui nhộn cho bé.",
        "created_at": date(2026, 6, 14),
    },
    {
        "id": 9,
        "name": "Kính lúp đồ chơi",
        "price": "40.000đ",
        "created_by": "Bảo Châu",
        "details": "Kính lúp nhỏ dành cho bé khám phá thiên nhiên.",
        "created_at": date(2026, 6, 13),
    },
    {
        "id": 10,
        "name": "Thú nhồi bông",
        "price": "55.000đ",
        "created_by": "Yến Nhi",
        "details": "Thú nhồi bông hình gấu, lông mềm mịn, size vừa tay bé.",
        "created_at": date(2026, 6, 12),
    },
]


class HomePage(QMainWindow):
    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        ui_path = self.root_dir + "/ui/home.ui"
        uic.loadUi(ui_path, self)

        self.account.clicked.connect(self.goto_account)
        self.search.clicked.connect(self.goto_search)

        self.set_danhsach_monhang()
        self.show()

    # ------------------ xử lý sự kiện ------------------
    def goto_account(self):
        from pages.account import AccountPage

        self.account_page = AccountPage(
            main_window=self.main_window, root_dir=self.root_dir, cur_acc=self.cur_acc
        )
        self.close()

    def goto_search(self):
        if self.search_input.text().strip() == "":
            self.show_message("Vui lòng điền từ khóa để tìm kiếm!")
            return

        from pages.search import SearchPage

        # ✅ Lưu vào self. để Python không xóa object khỏi bộ nhớ
        # Nếu chỉ viết: search_page = SearchPage(...) thì khi hàm kết thúc
        # Python sẽ garbage collect (xóa) object đó → cửa sổ tự đóng ngay!
        self.search_page = SearchPage(
            main_window=self.main_window,
            root_dir=self.root_dir,
            search_key=self.search_input.text().strip(),
        )
        # ✅ KHÔNG gọi self.close() ở đây → Home vẫn còn mở phía sau

    def set_danhsach_monhang(self):
        from pages.item_card import ItemCard

        # ✅ Giải thích: Grid layout sắp xếp theo hàng và cột (row, column)
        # Ví dụ: 3 cột → item 0 ở (row=0, col=0), item 1 ở (row=0, col=1), ...
        SO_COT = 3  # mỗi hàng hiển thị 3 card

        # ✅ Xóa widget placeholder (widget thừa được thêm sẵn trong Qt Designer)
        # Nếu không xóa, grid sẽ bị lệch hoặc thừa ô trống
        for i in reversed(range(self.gridLayout.count())):
            widget = self.gridLayout.itemAt(i).widget()
            if widget:
                widget.setParent(
                    None
                )  # tách widget ra khỏi layout (xóa khỏi giao diện)

        # ✅ Vòng for duyệt danh sách, dùng enumerate để lấy chỉ số (index)
        # enumerate([a, b, c]) → (0, a), (1, b), (2, c)
        for index, mon_hang in enumerate(danhsach_monhang):

            # ✅ Random ảnh 1 hoặc 2 vì data chỉ có 2 ảnh
            # random.choice([...]) → chọn ngẫu nhiên 1 phần tử trong danh sách
            so_anh = random.choice([1, 2])
            img_path = f"{self.root_dir}/assets/imgs/image_{so_anh}.jpg"

            # ✅ Gán đường dẫn ảnh vào data trước khi truyền vào card
            mon_hang_copy = {**mon_hang, "img": img_path}
            # {**mon_hang, "img": img_path} nghĩa là:
            # copy toàn bộ dict mon_hang, rồi thêm/ghi đè key "img"

            # Tạo card widget
            card = ItemCard(root_dir=self.root_dir, product_data=mon_hang_copy)

            # ✅ Tính vị trí hàng và cột trong grid
            row = index // SO_COT  # // là chia lấy phần nguyên: 0//3=0, 3//3=1, 6//3=2
            col = index % SO_COT  # %  là chia lấy phần dư:     0%3=0,  1%3=1,  2%3=2

            # Thêm card vào đúng ô trong grid
            self.gridLayout.addWidget(card, row, col)

        # ✅ Giữ cho các card không bị giãn ra khi còn ít item
        # addStretch() thêm khoảng trống co giãn vào cuối, đẩy các card lên trên
        # (chỉ dùng được với QVBoxLayout/QHBoxLayout, với QGridLayout thì bỏ qua)

    # ------------------ hàm hỗ trợ ------------------
    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
