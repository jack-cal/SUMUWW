# SUMUWW Wallet PC 1.0.15

Nút thường mở 10 kết nối đi. Phần lớn chuyển tiếp cả khối và giao dịch. Nút có thể dùng một kết nối dự phòng đã xác minh để chuyển tiếp khối và mở kết nối thứ 11 trong thời gian ngắn để tìm nút khác. Tổng giới hạn là 125 kết nối. Nút nhận tối đa 117 kết nối đến, hoặc 115 khi có 10 kết nối đi.


1 SMW = 100.000.000 yugeon. Phí tự động có ba mức dựa trên dữ liệu quan sát cục bộ, không bảo đảm thời gian xác nhận. Bạn có thể nhập mức phí yugeon/vB. Hãy kiểm tra phí cuối cùng và tổng số SMW trước khi gửi. Giao dịch bị từ chối không làm giảm số dư.

Với một đầu vào trị giá 1 SMW, phí phụ thuộc vào việc có cần trả lại tiền thừa hay không. Nếu đầu vào và các đầu ra đều là P2WPKH và mức phí là 1 yugeon/vB, gửi 0.99999890 SMW sẽ tốn 110 yugeon và không còn tiền thừa. Nếu gửi 0.8 SMW từ cùng đầu vào, giao dịch có thêm một đầu ra để trả tiền thừa và phí là 141 yugeon. Ví trả lại tiền thừa nếu số tiền còn lại sau khi trừ phí đạt mức tối thiểu. Mức này có tính đến chi phí sử dụng số tiền thừa về sau. Nếu thấp hơn mức đó, phần còn lại được cộng vào phí hiển thị trước khi bạn xác nhận. Với đầu vào ví dùng SegWit gốc (P2WPKH), phép ước tính dành tối đa 71 byte cho chữ ký, kể cả loại hàm băm.


`1 yugeon = 0.00000001 SMW`

`1 SMW = 100,000,000 yugeon`

Phí tự động dựa trên lượng dữ liệu đang chờ, dung lượng khối và mức ưu tiên của giao dịch. Không sử dụng phí từ các khối cũ. Khi hàng đợi ngắn, mức phí tối thiểu được giữ nguyên. Bản xem trước được cập nhật; bước xác nhận cuối cùng cố định phí. Dữ liệu phản ánh nút cục bộ đang kết nối, không phải mọi nút.

Lịch sử thay thế giao dịch do nút này ghi nhận được giữ lại sau khi khởi động lại ví. Giao dịch bị loại bỏ không ảnh hưởng đến số dư.


Lịch sử đào tách riêng phát hành mới, phí giao dịch và tổng phần thưởng của từng khối. Số tiền ví của bạn nhận được hiển thị riêng. Khi chỉ nhận một phần, hệ thống không tự suy đoán cách chia hai thành phần. Nút cung cấp 28 phương thức RPC, bao gồm ước tính phí, đồng thời xác minh và chuyển tiếp giao dịch đã ký.

<!-- payment-policy-20261116 -->

## Phí, giao dịch đã kiểm tra và khả năng tương thích

Phí bằng tổng giá trị đầu vào trừ tổng giá trị đầu ra. Ước tính chỉ tính đầu ra tiền thừa khi ví thực sự tạo khoản tiền thừa đạt ngưỡng quy định. Phần còn lại dưới ngưỡng được cộng vào phí; phí cuối cùng và tổng số tiền trừ khỏi ví được hiển thị để kiểm tra. Đơn vị mức phí là yugeon/vB. Kích thước ảo bằng trọng số giao dịch chia bốn rồi làm tròn lên.

Ví chỉ chọn đầu vào và đầu ra một lần, sau đó ký đúng phương án giao dịch đó. Khi bạn xác nhận, ví gửi giao dịch đã ký được lưu sẵn, không dựng lại giao dịch hay tính lại phí. Nếu báo phí hết hạn hoặc đầu vào đã được chi tiêu, bạn cần kiểm tra lại. Được chấp nhận vào hàng đợi cục bộ không có nghĩa là đã được xác nhận trong khối.

Với thanh toán P2WPKH thông thường, ví tạo chữ ký low-R và low-S dài tối đa 71 byte, bao gồm byte SIGHASH_ALL. Đây là chính sách ký và ước tính kích thước, không phải giới hạn đồng thuận mới đối với những chữ ký hợp lệ khác. Chữ ký ngắn hơn có thể làm kích thước ảo thực tế nhỏ hơn ước tính. Mức phí đề xuất vẫn dựa trên hàng đợi cục bộ; dùng cách tính kích thước tương tự Bitcoin không đồng nghĩa với dùng mức phí của mạng Bitcoin.

## Thành phần I2P trên Windows và kiểm tra bảo mật

Gói Windows chứa i2pd 3.0.0 chính thức cùng giá trị băm và chứng chỉ kết nối ban đầu đã cập nhật. Trong lần kiểm tra được ghi nhận, Defender vẫn phát hiện tệp thực thi I2P và ZIP gốc chính thức. Giá trị băm trùng với nguồn chính thức không chứng minh tệp an toàn hay chắc chắn là nhận diện nhầm. Ngoại lệ tệp cục bộ chỉ có hiệu lực trên máy đã đăng ký; gói công khai không tự thêm ngoại lệ. Máy khác vẫn có thể chặn các tệp này.

<!-- /payment-policy-20261116 -->

Sau khi nhận được phản hồi phiên bản hợp lệ, nút dành thời gian cho nút bên kia gửi xác nhận. Nếu hai kết nối đi đến cùng một nút, một đường kết nối khả dụng được giữ cho đến khi một trong hai hoàn tất đồng bộ. Công cụ tự kiểm tra chấp nhận khối có bằng chứng công việc hợp lệ trước khi nhận được bằng chứng kết nối. Sau đó, công cụ kiểm tra chữ ký của ba nhân chứng, việc chuyển tiếp bằng chứng kết nối và khả năng lưu giữ bằng chứng sau khi khởi động lại.
