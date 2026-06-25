from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6 import uic


class DetailsPage(QMainWindow):
    def __init__(self, main_window, root_dir, cur_acc, product_data):
        super().__init__()
        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc
        self.product_data = product_data  # ✅ Lưu lại để dùng trong các hàm khác

        # ✅ Sửa lỗi: file UI tên là details.ui (không phải details1.ui)
        # Kiểm tra lại tên file thật trong thư mục /ui/ của bạn nhé!
        ui_path = self.root_dir + "/ui/details.ui"
        uic.loadUi(ui_path, self)

        # Hiển thị nội dung sản phẩm lên UI
        self.set_product_info()

        # Gắn sự kiện nút BUY
        self.buy_btn.clicked.connect(self.handle_buy)

        self.show()

    # ------------------ xử lý sự kiện ------------------
    def set_product_info(self):
        # ✅ Hiển thị ảnh
        pixmap = QPixmap(self.product_data["img"])
        if not pixmap.isNull():
            # scale ảnh vừa khít kích thước label (481x301) giữ tỉ lệ
            # Qt.AspectRatioMode.KeepAspectRatio: giữ tỉ lệ, không méo ảnh
            from PyQt6.QtCore import Qt

            scaled = pixmap.scaled(
                481,
                301,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
                # SmoothTransformation: scale mượt hơn (dùng anti-aliasing)
                # FastTransformation: nhanh hơn nhưng ảnh có thể bị răng cưa
            )
            self.img.setPixmap(scaled)
        else:
            print(f"[WARN] Không load được ảnh: {self.product_data['img']}")

        # ✅ Hiển thị mô tả
        self.description.setText(self.product_data["details"])

        # ✅ Hiển thị người đăng — thêm prefix "Bởi: " cho rõ nghĩa
        self.created_by.setText(f"Bởi: {self.product_data['created_by']}")

        # ✅ Hiển thị ngày đăng bán
        # product_data["created_at"] là kiểu date(2026, 6, 21)
        # .strftime(): format ngày thành chuỗi theo định dạng tuỳ chọn
        # %d = ngày (21), %m = tháng (06), %Y = năm (2026)
        ngay = self.product_data["created_at"].strftime("%d/%m/%Y")
        self.created_at.setText(f"Ngày đăng bán: {ngay}")

        # ✅ Hiển thị tiêu đề cửa sổ = tên sản phẩm (tuỳ chọn, nhìn chuyên nghiệp hơn)
        self.setWindowTitle(self.product_data["name"])

    def handle_buy(self):
        # ✅ Kiểm tra đăng nhập trước khi mua
        if self.cur_acc is None:
            self.show_message("Bạn cần đăng nhập để mua hàng!")
            return

        # TODO: thêm logic mua hàng thật (gọi API, lưu đơn hàng, v.v.)
        ten = self.product_data["name"]
        gia = self.product_data["price"]
        self.show_message(f"Đặt mua thành công!\n\n{ten}\nGiá: {gia}")

    # ------------------ hàm hỗ trợ ------------------
    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Thông báo")
        msg.setText(message)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
