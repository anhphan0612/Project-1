# Project-1
Phần mềm OCR dịch màn hình thời gian thực

# Bài toán thực tế
Khi chơi game đa số người chơi phổ thông gặp vấn đề về ngôn ngữ, nhà phát hành có thể không hỗ trợ ngôn ngữ tiếng Việt trong game. Điều này xuất phát từ khối lượng văn bản khổng lồ mà nhiều game sở hữu dẫn đến chi phí dịch thuật là rất lớn. Bên cạnh đó, thị trường game Việt Nam vẫn là một thị trường ngách, không dễ để tìm một tựa game được chính nhà phát hành hỗ trợ tiếng Việt. Vấn đề càng rõ ràng hơn khi đó là tựa game có yếu tố cốt truyện. Việc ngôn ngữ không được hỗ trợ có thể khiến người chơi tải các bản crack, bản game đã bị sửa đổi (mod). Việc mod này thường nằm trong vùng xám điều khoản của đa số các game offline nhưng không phải game nào cũng vậy. OCR dịch màn hình thời gian thực trong các tựa game sẽ hỗ trợ nhóm đối tượng người chơi này, OCR này sử dụng External Overlay nên sẽ không can thiệp vào file game, từ đó hạn chế rủi ro ăn ban.

# Vấn đề
- Chiếm tài nguyên máy tính
- Độ chính xác có thể không cao, chất lượng bản dịch không tốt
- Văn phong có thể không nhất quán cũng như không phù hợp với thể loại game
- Tích hợp AI và build AI from scratch tốn tài nguyên
- Việc dịch ngôn ngữ không phải Latinh, điển hình là tiếng Trung có thể khó khăn hơn
- Có thể xung đột với các phần mềm đồ họa khác ví dụ DirectX hay Vulkan
- Thời gian phản hồi phải đủ nhanh

# Giải pháp tối ưu

# Công nghệ (tạm thời)
Python - Ngôn ngữ chính
OpenCV, numpy - Dùng để xử lý ảnh
Qt/PySide6 (maybe) - Giao diện, overlay
Tesseract/PaddleOCR (maybe) - OCR có sẵn
mss (maybe) - Chụp màn hình
    Scap (maybe): Sử dụng Rust cho việc chụp ảnh màn hình, tận dụng hiệu năng, đóng gói thông qua Maturin rồi gửi sang Python xử lý
Một mô hình dịch nào đó
