# SUMUWW · Ghi chú phiên bản

Với một đầu vào trị giá 1 SMW, phí phụ thuộc vào việc có cần trả lại tiền thừa hay không. Nếu đầu vào và các đầu ra đều là P2WPKH và mức phí là 1 yugeon/vB, gửi 0.99999890 SMW sẽ tốn 110 yugeon và không còn tiền thừa. Nếu gửi 0.8 SMW từ cùng đầu vào, giao dịch có thêm một đầu ra để trả tiền thừa và phí là 141 yugeon. Ví trả lại tiền thừa nếu số tiền còn lại sau khi trừ phí đạt mức tối thiểu. Mức này có tính đến chi phí sử dụng số tiền thừa về sau. Nếu thấp hơn mức đó, phần còn lại được cộng vào phí hiển thị trước khi bạn xác nhận. Với đầu vào ví dùng SegWit gốc (P2WPKH), phép ước tính dành tối đa 71 byte cho chữ ký, kể cả loại hàm băm.

0.57.61 · Khi đổi ngôn ngữ trong lúc ứng dụng đang chạy, biểu tượng trên thanh tác vụ Windows cũng thay đổi.

Nút thường mở 10 kết nối đi. Phần lớn chuyển tiếp cả khối và giao dịch. Nút có thể dùng một kết nối dự phòng đã xác minh để chuyển tiếp khối và mở kết nối thứ 11 trong thời gian ngắn để tìm nút khác. Tổng giới hạn là 125 kết nối. Nút nhận tối đa 117 kết nối đến, hoặc 115 khi có 10 kết nối đi. Ứng dụng trên máy tính hiện chỉ hiển thị tổng số nút đang kết nối. Mỗi thiết bị đào tự tạo khối. Nút trên máy tính chuyển tiếp các khối hoàn chỉnh và từ chối yêu cầu cấp việc đào cũng như kết quả tính toán do điện thoại gửi đến.

Khi khởi động lại, nút tiếp tục từ khối cuối cùng đã tự xác minh và kiểm tra các khối mới. Nếu bản ghi xác minh đã lưu bị thiếu hoặc không khớp, nút sẽ kiểm tra lại lịch sử đã lưu.

SUMUWW PC 0.57.61 · Nút xác thực, lưu trữ, truyền và cung cấp dữ liệu chuỗi.

## Định dạng chữ ký

SDK mã nguồn tùy chọn tạo giao dịch và kiểm tra chữ ký được cung cấp mà không cần khóa hay mạng. Đây không phải chương trình ký hoặc lệnh của nút. Giới hạn thanh toán P2WPKH thuộc định dạng ví dụ, không phải nút. Ví cá nhân hiện có vẫn dùng được.

## API RPC và HTTP

validateaddress kiểm tra checksum và mạng đã chọn. decoded_only của decoderawtransaction chỉ nghĩa là giải mã, không xác nhận chữ ký hay giao dịch. OP_RETURN lưu dữ liệu cho chương trình ngoài. Nút có thêm truy vấn phí, kiểm tra trước khi gửi, trạng thái thay thế RBF và đọc dữ liệu theo thứ tự khối. Giao dịch thay thế được xác minh trước khi xóa giao dịch đang chờ. Đa chữ ký và đầu ra khóa đã được triển khai để thử kích hoạt trong môi trường riêng; chưa kích hoạt trên mạng công khai.

## Kiểm chứng

Cài các phụ thuộc rồi chạy python examples/node_contract.py từ mã nguồn. Khóa thử nghiệm công khai và regtest tạm thời kiểm tra gửi, từ chối, xác nhận, tái tổ chức và lưu giữ dữ liệu. Không dùng tiền thật, hồ sơ người dùng hoặc thiết bị ký phần cứng.

[Tài liệu](README.html) · [Giao diện nút](EXCHANGE_INTEGRATION.html) · [API RPC và HTTP](RPC_API.html) · [Vận hành nút](NETWORK_RUNBOOK.html) · [Kiểm chứng](EXCHANGE_EXAMPLES.html)

[Tài liệu chi tiết tiếng Anh](../../../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../../../API_CONTRACT.json) · [vectors.json](../../../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Phí, giao dịch đã kiểm tra và khả năng tương thích

Phí bằng tổng giá trị đầu vào trừ tổng giá trị đầu ra. Ước tính chỉ tính đầu ra tiền thừa khi ví thực sự tạo khoản tiền thừa đạt ngưỡng quy định. Phần còn lại dưới ngưỡng được cộng vào phí; phí cuối cùng và tổng số tiền trừ khỏi ví được hiển thị để kiểm tra. Đơn vị mức phí là yugeon/vB. Kích thước ảo bằng trọng số giao dịch chia bốn rồi làm tròn lên.

Ví chỉ chọn đầu vào và đầu ra một lần, sau đó ký đúng phương án giao dịch đó. Khi bạn xác nhận, ví gửi giao dịch đã ký được lưu sẵn, không dựng lại giao dịch hay tính lại phí. Nếu báo phí hết hạn hoặc đầu vào đã được chi tiêu, bạn cần kiểm tra lại. Được chấp nhận vào hàng đợi cục bộ không có nghĩa là đã được xác nhận trong khối.

Với thanh toán P2WPKH thông thường, ví tạo chữ ký low-R và low-S dài tối đa 71 byte, bao gồm byte SIGHASH_ALL. Đây là chính sách ký và ước tính kích thước, không phải giới hạn đồng thuận mới đối với những chữ ký hợp lệ khác. Chữ ký ngắn hơn có thể làm kích thước ảo thực tế nhỏ hơn ước tính. 

<!-- /payment-policy-20261116 -->
