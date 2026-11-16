# Phí, giao dịch đã kiểm tra và khả năng tương thích

SUMUWW · 2026-11-16

<!-- payment-policy-20261116 -->

## Phí, giao dịch đã kiểm tra và khả năng tương thích

Phí bằng tổng giá trị đầu vào trừ tổng giá trị đầu ra. Ước tính chỉ tính đầu ra tiền thừa khi ví thực sự tạo khoản tiền thừa đạt ngưỡng quy định. Phần còn lại dưới ngưỡng được cộng vào phí; phí cuối cùng và tổng số tiền trừ khỏi ví được hiển thị để kiểm tra. Đơn vị mức phí là yugeon/vB. Kích thước ảo bằng trọng số giao dịch chia bốn rồi làm tròn lên.

Ví chỉ chọn đầu vào và đầu ra một lần, sau đó ký đúng phương án giao dịch đó. Khi bạn xác nhận, ví gửi giao dịch đã ký được lưu sẵn, không dựng lại giao dịch hay tính lại phí. Nếu báo phí hết hạn hoặc đầu vào đã được chi tiêu, bạn cần kiểm tra lại. Được chấp nhận vào hàng đợi cục bộ không có nghĩa là đã được xác nhận trong khối.

Với thanh toán P2WPKH thông thường, ví tạo chữ ký low-R và low-S dài tối đa 71 byte, bao gồm byte SIGHASH_ALL. Đây là chính sách ký và ước tính kích thước, không phải giới hạn đồng thuận mới đối với những chữ ký hợp lệ khác. Chữ ký ngắn hơn có thể làm kích thước ảo thực tế nhỏ hơn ước tính. Mức phí đề xuất vẫn dựa trên hàng đợi cục bộ; dùng cách tính kích thước tương tự Bitcoin không đồng nghĩa với dùng mức phí của mạng Bitcoin.

## Thành phần I2P trên Windows và kiểm tra bảo mật

Gói Windows chứa i2pd 3.0.0 chính thức cùng giá trị băm và chứng chỉ kết nối ban đầu đã cập nhật. Trong lần kiểm tra được ghi nhận, Defender vẫn phát hiện tệp thực thi I2P và ZIP gốc chính thức. Giá trị băm trùng với nguồn chính thức không chứng minh tệp an toàn hay chắc chắn là nhận diện nhầm. Ngoại lệ tệp cục bộ chỉ có hiệu lực trên máy đã đăng ký; gói công khai không tự thêm ngoại lệ. Máy khác vẫn có thể chặn các tệp này.

## Tương thích chữ ký Android

Định dạng tệp ví, địa chỉ và số coin hiện có không thay đổi. Có thể khôi phục bản sao lưu ví được mã hóa cũ trong ứng dụng mới để tiếp tục dùng cùng một ví. Nút Android 0.6.102 và ví 1.1.13 dùng khóa ký phát hành mới. Chúng không thể thay thế bản cài đặt được ký bằng khóa khác. Hãy giữ ứng dụng cũ và dữ liệu cho đến khi có bản sao lưu ví được mã hóa và cách khôi phục hoạt động được. Đừng gỡ ứng dụng cũ chỉ để ép cài bản cập nhật.

<!-- /payment-policy-20261116 -->
