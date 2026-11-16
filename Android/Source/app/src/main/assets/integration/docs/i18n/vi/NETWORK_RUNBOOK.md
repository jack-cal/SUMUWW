# SUMUWW Android 0.6.103 · Vận hành nút

Khi khởi động lại, nút tiếp tục từ khối cuối cùng đã tự xác minh và kiểm tra các khối mới. Nếu bản ghi xác minh đã lưu bị thiếu hoặc không khớp, nút sẽ kiểm tra lại lịch sử đã lưu.

SUMUWW Android 0.6.103 · Nút xác thực, lưu trữ, truyền và cung cấp dữ liệu chuỗi.

## Mạng và địa chỉ

Mạng công khai là `sumuww`, bí danh nội bộ là `dora`. Kiểm tra hash khối khởi nguyên bên dưới. Địa chỉ gốc dùng witness v0 P2WPKH và HASH160 của khóa công khai secp256k1 nén. Không bắt buộc memo hay tag. Từ chối sai mạng và checksum không hợp lệ. Ghi lại nhánh HD nhận/tiền thừa và chỉ số; không giả định đường dẫn suy dẫn của Bitcoin.

## Tra cứu giao dịch và khối

`getrawtransaction` tìm trong chuỗi hoạt động và mempool, không tìm giao dịch chỉ còn ở nhánh bị loại. Đầu vào chỉ ra đầu ra trước đó, không phải một địa chỉ người gửi duy nhất. `getblock` nhận `verbose` Boolean; khối lưu nhưng không hoạt động có `active=false`, `confirmations=-1`. Vẫn lấy được giao dịch thô qua hash khối. `findspendingtransaction` chỉ tìm khoản chi đã xác nhận trong chuỗi hoạt động; null không chứng minh khả dụng. Kiểm tra `gettxout` với `include_mempool=true`. Số xác nhận và trạng thái hoạt động có thể đổi sau tái tổ chức.

[API_CONTRACT.json](../../../API_CONTRACT.json)

<!-- payment-policy-20261116 -->

## Phí, giao dịch đã kiểm tra và khả năng tương thích

Phí bằng tổng giá trị đầu vào trừ tổng giá trị đầu ra. Ước tính chỉ tính đầu ra tiền thừa khi ví thực sự tạo khoản tiền thừa đạt ngưỡng quy định. Phần còn lại dưới ngưỡng được cộng vào phí; phí cuối cùng và tổng số tiền trừ khỏi ví được hiển thị để kiểm tra. Đơn vị mức phí là yugeon/vB. Kích thước ảo bằng trọng số giao dịch chia bốn rồi làm tròn lên.

Ví chỉ chọn đầu vào và đầu ra một lần, sau đó ký đúng phương án giao dịch đó. Khi bạn xác nhận, ví gửi giao dịch đã ký được lưu sẵn, không dựng lại giao dịch hay tính lại phí. Nếu báo phí hết hạn hoặc đầu vào đã được chi tiêu, bạn cần kiểm tra lại. Được chấp nhận vào hàng đợi cục bộ không có nghĩa là đã được xác nhận trong khối.

Với thanh toán P2WPKH thông thường, ví tạo chữ ký low-R và low-S dài tối đa 71 byte, bao gồm byte SIGHASH_ALL. Đây là chính sách ký và ước tính kích thước, không phải giới hạn đồng thuận mới đối với những chữ ký hợp lệ khác. Chữ ký ngắn hơn có thể làm kích thước ảo thực tế nhỏ hơn ước tính. Mức phí đề xuất vẫn dựa trên hàng đợi cục bộ; dùng cách tính kích thước tương tự Bitcoin không đồng nghĩa với dùng mức phí của mạng Bitcoin.

## Tương thích chữ ký Android

Định dạng tệp ví, địa chỉ và số coin hiện có không thay đổi. Có thể khôi phục bản sao lưu ví được mã hóa cũ trong ứng dụng mới để tiếp tục dùng cùng một ví. Nút Android 0.6.103 và ví 1.1.14 dùng khóa ký phát hành mới. Chúng không thể thay thế bản cài đặt được ký bằng khóa khác. Hãy giữ ứng dụng cũ và dữ liệu cho đến khi có bản sao lưu ví được mã hóa và cách khôi phục hoạt động được. Đừng gỡ ứng dụng cũ chỉ để ép cài bản cập nhật.

<!-- /payment-policy-20261116 -->

Sau khi nhận được phản hồi phiên bản hợp lệ, nút dành thời gian cho nút bên kia gửi xác nhận. Nếu hai kết nối đi đến cùng một nút, một đường kết nối khả dụng được giữ cho đến khi một trong hai hoàn tất đồng bộ. Công cụ tự kiểm tra chấp nhận khối có bằng chứng công việc hợp lệ trước khi nhận được bằng chứng kết nối. Sau đó, công cụ kiểm tra chữ ký của ba nhân chứng, việc chuyển tiếp bằng chứng kết nối và khả năng lưu giữ bằng chứng sau khi khởi động lại.
