# SUMUWW Android 0.6.103 · Ghi chú phiên bản

Với một đầu vào trị giá 1 SMW, phí phụ thuộc vào việc có cần trả lại tiền thừa hay không. Nếu đầu vào và các đầu ra đều là P2WPKH và mức phí là 1 yugeon/vB, gửi 0.99999890 SMW sẽ tốn 110 yugeon và không còn tiền thừa. Nếu gửi 0.8 SMW từ cùng đầu vào, giao dịch có thêm một đầu ra để trả tiền thừa và phí là 141 yugeon. Ví trả lại tiền thừa nếu số tiền còn lại sau khi trừ phí đạt mức tối thiểu. Mức này có tính đến chi phí sử dụng số tiền thừa về sau. Nếu thấp hơn mức đó, phần còn lại được cộng vào phí hiển thị trước khi bạn xác nhận. Với đầu vào ví dùng SegWit gốc (P2WPKH), phép ước tính dành tối đa 71 byte cho chữ ký, kể cả loại hàm băm.

Khi khởi động lại, nút tiếp tục từ khối cuối cùng đã tự xác minh và kiểm tra các khối mới. Nếu bản ghi xác minh đã lưu bị thiếu hoặc không khớp, nút sẽ kiểm tra lại lịch sử đã lưu.

SUMUWW Android 0.6.103 · Nút xác thực, lưu trữ, truyền và cung cấp dữ liệu chuỗi.

Đặc tả API mô tả lõi nút tích hợp. Ứng dụng Android không có màn hình cấu hình RPC.

## API RPC và HTTP

validateaddress kiểm tra checksum và mạng đã chọn. decoded_only của decoderawtransaction chỉ nghĩa là giải mã, không xác nhận chữ ký hay giao dịch. OP_RETURN lưu dữ liệu cho chương trình ngoài. Nút có thêm truy vấn phí, kiểm tra trước khi gửi, trạng thái thay thế RBF và đọc dữ liệu theo thứ tự khối. Giao dịch thay thế được xác minh trước khi xóa giao dịch đang chờ. Đa chữ ký và đầu ra khóa đã được triển khai để thử kích hoạt trong môi trường riêng; chưa kích hoạt trên mạng công khai.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Phí, giao dịch đã kiểm tra và khả năng tương thích

Phí bằng tổng giá trị đầu vào trừ tổng giá trị đầu ra. Ước tính chỉ tính đầu ra tiền thừa khi ví thực sự tạo khoản tiền thừa đạt ngưỡng quy định. Phần còn lại dưới ngưỡng được cộng vào phí; phí cuối cùng và tổng số tiền trừ khỏi ví được hiển thị để kiểm tra. Đơn vị mức phí là yugeon/vB. Kích thước ảo bằng trọng số giao dịch chia bốn rồi làm tròn lên.

Ví chỉ chọn đầu vào và đầu ra một lần, sau đó ký đúng phương án giao dịch đó. Khi bạn xác nhận, ví gửi giao dịch đã ký được lưu sẵn, không dựng lại giao dịch hay tính lại phí. Nếu báo phí hết hạn hoặc đầu vào đã được chi tiêu, bạn cần kiểm tra lại. Được chấp nhận vào hàng đợi cục bộ không có nghĩa là đã được xác nhận trong khối.

Với thanh toán P2WPKH thông thường, ví tạo chữ ký low-R và low-S dài tối đa 71 byte, bao gồm byte SIGHASH_ALL. Đây là chính sách ký và ước tính kích thước, không phải giới hạn đồng thuận mới đối với những chữ ký hợp lệ khác. Chữ ký ngắn hơn có thể làm kích thước ảo thực tế nhỏ hơn ước tính. 

## Tương thích chữ ký Android

Định dạng tệp ví, địa chỉ và số coin hiện có không thay đổi. Có thể khôi phục bản sao lưu ví được mã hóa cũ trong ứng dụng mới để tiếp tục dùng cùng một ví. Nút Android 0.6.103 và ví 1.1.14 dùng khóa ký phát hành mới. Chúng không thể thay thế bản cài đặt được ký bằng khóa khác. Hãy giữ ứng dụng cũ và dữ liệu cho đến khi có bản sao lưu ví được mã hóa và cách khôi phục hoạt động được. Đừng gỡ ứng dụng cũ chỉ để ép cài bản cập nhật.

<!-- /payment-policy-20261116 -->
