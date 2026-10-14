Phần mềm thực hiện lặp lại quy trình sau:
Capture (tức lấy ảnh màn hình) -> Crop vùng chữ, thoại cần thiết -> Phát hiện nếu có sự thay đổi -> Tiền xử lý -> OCR -> Làm sạch text -> Dịch (cache lại) -> Overlay hiển thị

Phần mềm gồm 3 luồng chính:
- Capture + diff:  Chụp, crop và diff sẽ do Rust xử lý
- OCR: Thử cả PaddleOCR, RapidOCR và Tesseract để chọn OCR nào phù hợp trên tập game test ban đầu, so sánh lỗi dịch sai, tốc độ
- Dịch + Overlay

Độ khó thiết kế đối với các game có thoại nhanh sẽ khó hơn với game dạng Visual Novel hay RPG thoại.

- Capture -> Crop:
    Input: Khung hình thô (frame) từ bước capture
    Output: ROI, tọa độ, phần ảnh con cần thiết
- Crop -> Diff:
    Input: Region (ROI)
    Output: Region (ROI)
    Diff giữ hash của lần trước, chỉ phát khi đã ổn định
- -> OCR (bao gồm tiền xử lý):
    Input: Region
    Output: Văn bản dạng text
- -> Hậu xử lý:
    Input: Văn bản dạng text từ OCR
    Output: Văn bản dạng text (hoặc thay đổi định dạng) sau khi đã làm sạch ví dụ lọc nhiễu, lọc bỏ ký tự rác, lọc bỏ lỗi chính tả, tách tên người nói...
- -> Dịch:
    Tra cache
- -> Overlay