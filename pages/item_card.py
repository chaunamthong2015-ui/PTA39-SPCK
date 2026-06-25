from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPixmap  # ← dùng để load ảnh vào QLabel
from PyQt6 import uic


class ItemCard(QWidget):
    def __init__(self, root_dir, product_data):
        super().__init__()
        self.root_dir = root_dir
        self.product_data = product_data

        ui_path = self.root_dir + "/ui/product_card.ui"
        uic.loadUi(ui_path, self)

        self.get_product_info()

        # ✅ Sửa lỗi: phải là .clicked.connect(), không phải .connect()
        self.detail.clicked.connect(self.goto_details)

        # ✅ KHÔNG gọi self.show() ở đây vì ItemCard là widget con (không phải cửa sổ độc lập)
        # Gọi show() trên widget con sẽ tạo ra cửa sổ riêng thay vì hiện trong home

    # ------------------ xử lý sự kiện ------------------
    def get_product_info(self):
        # ✅ Hiển thị ảnh lên label (QLabel)
        # QPixmap: class dùng để load và hiển thị ảnh trong Qt
        pixmap = QPixmap(self.product_data["img"])
        if pixmap.isNull():
            # Nếu không load được ảnh → không làm gì (giữ ảnh mặc định từ .ui)
            print(f"[WARN] Không load được ảnh: {self.product_data['img']}")
        else:
            # scaledToWidth: tự động scale ảnh vừa với chiều rộng 200px
            self.label.setPixmap(pixmap.scaled(200, 200))

        # ✅ Hiển thị tên sản phẩm lên label_2
        self.label_2.setText(self.product_data["name"])

        # ✅ Hiển thị giá lên label_3
        self.label_3.setText(self.product_data["price"])

    def goto_details(self):
        from pages.details import DetailsPage

        # ✅ ItemCard không có self.main_window và self.cur_acc
        # → cần truyền vào từ ngoài, hoặc lấy từ parent window
        # Tạm thời dùng None nếu chưa có, nhớ cập nhật sau
        self.details_page = DetailsPage(
            main_window=None,  # TODO: truyền main_window vào ItemCard
            root_dir=self.root_dir,
            cur_acc=None,  # TODO: truyền cur_acc vào ItemCard
            product_data=self.product_data,
        )
        self.details_page.show()
