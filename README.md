# Thông tin ảnh được ghi lại sau khi chạy chương trình

## Ảnh gốc
Kích thước: 736x1307
Số kênh: 3
Tổng số pixel: 961952

## Ảnh xám
Kích thước: 736x1307
Số kênh: 1
Tổng số pixel: 961952

## Ảnhgiảm nhiễu
Kích thước: 736x1307
Số kênh: 1
Tổng số pixel: 961952

## Dò biên Sobel
Kích thước: 736x1307
Số kênh: 1
Tổng số pixel: 961952

## Dò biên Laplacian
Kích thước: 736x1307
Số kênh: 1
Tổng số pixel: 961952

-Nhập thư viện cần thiết
sử dụng cv2 (OpenCV) cho xử lý ảnh và numpy để làm việc với mảng
-Đọc ảnh
đọc một bức ảnh và chuyển đổi nó sang dạng ảnh xám (grayscale)
ảnh xám giúp đơn giản hóa viêc xử lý vì dùng 1 kênh màu
-Dò biên bằng toán tử Sobel
Gx = [-1 0 1]             Gy = [ 1  2  1]
     [-2 0 2]                  [ 0  0  0]
     [-1 0 1]                  [-1 -2 -1]
Để tính độ lớn grandient:
G = sqrt(Gx^2+ Gy^2)

