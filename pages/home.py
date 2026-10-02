from datetime import date
import random  # ← dùng để random số 1 hoặc 2

from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import uic

# ✅ Danh sách 10 món hàng
# img để là placeholder "1" hoặc "2" — sẽ random khi tạo card
danhsach_monhang = [
    {
        "id": 1,
        "name": "Banh tròn màu sắc",
        "price": "20.000đ",
        "created_by": "Nam Thông",
        "details": "Đồ chơi bằng nhựa PP nguyên sinh an toàn cho trẻ nhỏ, nhiều màu sắc.",
        "created_at": date(2026, 6, 21),
        "img": "assets/imgs/image_1.jpg"
    },
    {
        "id": 2,
        "name": "Xe đồ chơi mini",
        "price": "35.000đ",
        "created_by": "Minh Anh",
        "details": "Xe mô hình nhỏ bằng hợp kim, sơn màu bền đẹp.",
        "created_at": date(2026, 6, 20),
        "img": "assets/imgs/image_2.jpg"
    },
    {
        "id": 3,
        "name": "Búp bê vải",
        "price": "50.000đ",
        "created_by": "Thu Hà",
        "details": "Búp bê may bằng vải cotton mềm mại, an toàn cho bé.",
        "created_at": date(2026, 6, 19),
        "img": "assets/imgs/image_3.jpg"
    },
    {
        "id": 4,
        "name": "Xếp hình gỗ",
        "price": "45.000đ",
        "created_by": "Quốc Bảo",
        "details": "Bộ xếp hình bằng gỗ tự nhiên, giúp phát triển tư duy.",
        "created_at": date(2026, 6, 18),
        "img": "assets/imgs/image_4.jpg"
    },
    {
        "id": 5,
        "name": "Bóng cao su",
        "price": "15.000đ",
        "created_by": "Lan Nhi",
        "details": "Bóng cao su nhiều màu, đàn hồi tốt, an toàn.",
        "created_at": date(2026, 6, 17),
        "img": "assets/imgs/image_5.jpg"
    },
    {
        "id": 6,
        "name": "Đất nặn màu",
        "price": "25.000đ",
        "created_by": "Hùng Cường",
        "details": "Đất nặn an toàn không độc hại, bộ 12 màu.",
        "created_at": date(2026, 6, 16),
        "img": "assets/imgs/image_6.jpg"
    },
    {
        "id": 7,
        "name": "Tranh tô màu",
        "price": "18.000đ",
        "created_by": "Diệu Linh",
        "details": "Tập tranh tô màu chủ đề động vật, 20 trang.",
        "created_at": date(2026, 6, 15),
        "img": "assets/imgs/image_7.jpg"
    },
    {
        "id": 8,
        "name": "Trống lắc tay",
        "price": "30.000đ",
        "created_by": "Phúc An",
        "details": "Trống lắc nhỏ bằng gỗ, âm thanh vui nhộn cho bé.",
        "created_at": date(2026, 6, 14),
        "img": "assets/imgs/image_8.jpg"
    },
    {
        "id": 9,
        "name": "Kính lúp đồ chơi",
        "price": "40.000đ",
        "created_by": "Bảo Châu",
        "details": "Kính lúp nhỏ dành cho bé khám phá thiên nhiên.",
        "created_at": date(2026, 6, 13),
        "img": "assets/imgs/image_9.jpg"
    },
    {
        "id": 10,
        "name": "Thú nhồi bông",
        "price": "55.000đ",
        "created_by": "Yến Nhi",
        "details": "Thú nhồi bông hình gấu, lông mềm mịn, size vừa tay bé.",
        "created_at": date(2026, 6, 12),
        "img": "assets/imgs/image_10.jpg"
    },
    {
    "id": 11,
    "name": "Bộ cờ vua mini",
    "price": "60.000đ",
    "created_by": "Hoàng Nam",
    "details": "Bộ cờ vua kích thước nhỏ, giúp rèn luyện tư duy logic.",
    "created_at": date(2026, 6, 11),
    "img": "assets/imgs/image_11.jpg"
    },
    {
    "id": 12,
    "name": "Rubik 3x3",
    "price": "25.000đ",
    "created_by": "Gia Huy",
    "details": "Khối Rubik 3x3 xoay trơn, phù hợp cho trẻ em và người mới chơi.",
    "created_at": date(2026, 6, 10),
    "img": "assets/imgs/image_12.jpg"
    },
    {
    "id": 13,
    "name": "Bộ bác sĩ nhí",
    "price": "75.000đ",
    "created_by": "Khánh Linh",
    "details": "Bộ đồ chơi bác sĩ gồm ống nghe, nhiệt kế và nhiều dụng cụ mô phỏng.",
    "created_at": date(2026, 6, 9),
    "img": "assets/imgs/image_13.jpg"
    },
    {
    "id": 14,
    "name": "Bộ nấu ăn mini",
    "price": "100.000đ",
    "created_by": "Mai Anh",
    "details": "Bộ đồ chơi nhà bếp nhiều dụng cụ nhỏ, màu sắc tươi sáng.",
    "created_at": date(2026, 6, 8),
    "img": "assets/imgs/image_14.jpg"
    },
    {
    "id": 15,
    "name": "Máy bay đồ chơi",
    "price": "45.000đ",
    "created_by": "Đức Anh",
    "details": "Máy bay mô hình nhỏ gọn, thiết kế đẹp và chắc chắn.",
    "created_at": date(2026, 6, 7),
    "img": "assets/imgs/image_15.jpg"
    },
    {
    "id": 16,
    "name": "Tàu hỏa mini",
    "price": "50.000đ",
    "created_by": "Tuấn Kiệt",
    "details": "Tàu hỏa đồ chơi nhiều toa, phù hợp cho trẻ yêu thích phương tiện giao thông.",
    "created_at": date(2026, 6, 6),
    "img": "assets/imgs/image_16.jpg"
    },
    {
    "id": 17,
    "name": "Bộ domino màu",
    "price": "35.000đ",
    "created_by": "Ngọc Hân",
    "details": "Bộ domino nhiều màu giúp trẻ rèn khả năng quan sát và tư duy.",
    "created_at": date(2026, 6, 5),
    "img": "assets/imgs/image_17.jpg"
    },
    {
    "id": 18,
    "name": "Bộ lắp ráp robot",
    "price": "200.000đ",
    "created_by": "Thanh Tùng",
    "details": "Bộ lắp ráp robot nhiều chi tiết, giúp phát triển khả năng sáng tạo.",
    "created_at": date(2026, 6, 4),
    "img": "assets/imgs/image_18.jpg"
    },
    {
    "id": 19,
    "name": "Súng phun nước",
    "price": "30.000đ",
    "created_by": "Nhật Minh",
    "details": "Đồ chơi phun nước nhỏ gọn, thích hợp cho các hoạt động ngoài trời.",
    "created_at": date(2026, 6, 3),
    "img": "assets/imgs/image_19.jpg"
    },
    {
    "id": 20,
    "name": "Diều giấy mini",
    "price": "20.000đ",
    "created_by": "Hải Đăng",
    "details": "Diều giấy nhiều màu sắc, nhẹ và dễ điều khiển.",
    "created_at": date(2026, 6, 2),
    "img": "assets/imgs/image_20.jpg"
    },
    {
    "id": 21,
    "name": "Bộ câu cá nam châm",
    "price": "55.000đ",
    "created_by": "Thảo Vy",
    "details": "Trò chơi câu cá bằng nam châm giúp trẻ luyện sự khéo léo.",
    "created_at": date(2026, 6, 1),
    "img": "assets/imgs/image_21.jpg"
    },
    {
    "id": 22,
    "name": "Bộ xếp hình chữ cái",
    "price": "40.000đ",
    "created_by": "Phương Anh",
    "details": "Bộ chữ cái nhiều màu giúp trẻ làm quen với chữ và từ đơn giản.",
    "created_at": date(2026, 5, 31),
    "img": "assets/imgs/image_22.jpg"
    },
    {
    "id": 23,
    "name": "Máy xúc đồ chơi",
    "price": "70.000đ",
    "created_by": "Duy Khánh",
    "details": "Mô hình máy xúc công trình với cần xúc có thể chuyển động.",
    "created_at": date(2026, 5, 26),
    "img": "assets/imgs/image_23.jpg"
},
    {
    "id": 24,
    "name": "Bảng vẽ nam châm",
    "price": "65.000đ",
    "created_by": "Tú Anh",
    "details": "Bảng vẽ nam châm có bút và khuôn hình, dễ dàng xóa để sử dụng lại.",
    "created_at": date(2026, 5, 29),
    "img": "assets/imgs/image_24.jpg"
    }
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

        SO_COT = 3

        # ✅ Lấy layout ra biến riêng (thay vì gọi trực tiếp trên widget)
        layout = self.items_container.layout()

        # ✅ Xóa widget placeholder cũ
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for index, mon_hang in enumerate(danhsach_monhang):
            img_path = f"{ self.root_dir}/" + mon_hang["img"]
            mon_hang_copy = {**mon_hang, "img": img_path}
            card = ItemCard(root_dir=self.root_dir, product_data=mon_hang_copy)

            row = index // SO_COT
            col = index % SO_COT

            # ✅ Gọi addWidget trên layout, không phải trên container
            layout.addWidget(card, row, col)

    # ------------------ hàm hỗ trợ ------------------
    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()