import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def read_image(image_path):
    """Đọc ảnh và chuyển đổi sang ảnh xám."""
    image = cv2.imread(image_path)
    # Chuyển đổi ảnh từ BGR sang RGB để tránh ám màu khi hiển thị
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return rgb_image, gray_image


def gaussian_blur(gray_image, kernel_size=(5, 5), sigma=0):
    """Giảm nhiễu bằng cách sử dụng bộ lọc Gaussian."""
    return cv2.GaussianBlur(gray_image, kernel_size, sigma)


def sobel_edge_detection(gray_image):
    """Thực hiện dò biên bằng toán tử Sobel."""
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    return np.uint8(sobel_magnitude)


def laplacian_edge_detection(gray_image):
    """Thực hiện dò biên bằng toán tử Laplacian Gaussian."""
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    return np.uint8(np.absolute(laplacian))


def get_image_info(image, title):
    """Lấy thông tin của ảnh và lưu vào README.md"""
    # Lấy thông tin của ảnh
    height, width = image.shape[:2]
    num_channels = image.shape[2] if len(image.shape) == 3 else 1
    total_pixels = width * height  # Tính tổng số pixel
    info = (f"## {title}\n"
            f"Kích thước: {width}x{height}\n"
            f"Số kênh: {num_channels}\n"
            f"Tổng số pixel: {total_pixels}\n\n")

    # Ghi thông tin vào tệp README.md với mã hóa UTF-8
    with open('./README.md', 'a', encoding='utf-8') as file:
        file.write(info)




def display_and_save_images(images, titles, output_path, fig_size=(15, 10), dpi=100):
    """Hiển thị các ảnh và lưu vào file."""
    num_images = len(images)

    # Tạo một figure với kích thước và DPI tùy chỉnh
    plt.figure(figsize=fig_size, dpi=dpi)

    for i, (img, title) in enumerate(zip(images, titles)):
        # Hiển thị ảnh
        plt.subplot(1, num_images, i + 1)
        plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        plt.title(title, fontsize=16)
        plt.axis('off')  # Ẩn các trục

        # Lưu thông tin ảnh vào file README.md
        get_image_info(img, title)

    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()  # Hiển thị ảnh
    plt.close()  # Đóng hình để giải phóng bộ nhớ


def main():
    """Hàm chính để chạy chương trình."""
    image_path = 'images/XLA.jpg'  # Đường dẫn đến ảnh X-quang mẫu
    output_path = 'output/processed_images.png'  # Đường dẫn lưu ảnh kết quả

    # Xóa nội dung cũ của README.md nếu có và sử dụng encoding UTF-8
    with open('./README.md', 'w', encoding='utf-8') as file:
        file.write("# Thông tin ảnh\n\n")

    # Bước 1: Đọc ảnh
    original_image, gray_image = read_image(image_path)

    # Bước 2: Giảm nhiễu
    denoised_image = gaussian_blur(gray_image)

    # Bước 3: Dò biên bằng Sobel
    sobel_image = sobel_edge_detection(denoised_image)

    # Bước 4: Dò biên bằng Laplacian
    laplacian_image = laplacian_edge_detection(denoised_image)

    # Hiển thị các bước xử lý và lưu vào file
    images_to_display = [original_image, gray_image, denoised_image, sobel_image, laplacian_image]
    titles = ['Ảnh gốc', 'Ảnh xám', 'Ảnhgiảm nhiễu', 'Dò biên Sobel', 'Dò biên Laplacian']

    # Tùy chỉnh kích thước của hình hiển thị ở đây (fig_size)
    display_and_save_images(images_to_display, titles, output_path, fig_size=(20, 10), dpi=200)

if __name__ == "__main__":
    # Tạo thư mục output nếu chưa tồn tại
    os.makedirs('output', exist_ok=True)
    main()  # Chạy chương trình
