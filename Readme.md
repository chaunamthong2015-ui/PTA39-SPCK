# 🧸 Shop Đồ Chơi - Nam Thông

Ứng dụng bán đồ chơi trẻ em viết bằng **Python + PyQt6**, giao diện thiết kế bằng **Qt Designer**, dữ liệu lưu trong **file JSON**.

## Chức năng
- Đăng ký / đăng nhập (tài khoản lưu trong `data/users.json`)
- Trang chủ: hiển thị danh sách đồ chơi (đọc từ `data/products.json`)
- Tìm kiếm đồ chơi theo tên hoặc mô tả
- Xem chi tiết và thêm vào giỏ hàng
- Giỏ hàng: tăng / giảm số lượng, xóa món, tính tổng tiền + phí ship
- Thanh toán: điền thông tin giao hàng, đặt hàng (lưu vào `data/orders.json`)
- Lịch sử mua hàng

## Cấu trúc thư mục
```
assets/       hình ảnh (imgs), biểu tượng (icons) và style.qss (giao diện chung)
pages/        các trang: login, register, home, search, details, gio_hang, checkout, lich_su, account
ui/           file .ui thiết kế bằng Qt Designer
components/   các thẻ (card) hiển thị trong danh sách: TheSanPham, TheMonTrongGio, TheDonHang
entities/     class dữ liệu: NguoiDung, SanPham, DonHang + class quản lý QuanLyNguoiDung, QuanLySanPham, QuanLyDonHang
data/         file JSON lưu dữ liệu + data_io.py (đọc/ghi JSON)
app.py        file chạy chương trình
```

## Cài đặt và chạy (Windows)
1. Cài Python 3.10 trở lên.
2. Mở Terminal tại thư mục dự án, cài thư viện:
   ```
   pip install -r Requirements.txt
   ```
3. Chạy app:
   ```
   python app.py
   ```

## Tài khoản dùng thử
- Email: `thong@gmail.com`
- Mật khẩu: `1234567`
