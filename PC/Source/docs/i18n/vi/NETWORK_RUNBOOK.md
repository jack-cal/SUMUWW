# SUMUWW · Vận hành nút

Nút thường mở 10 kết nối đi. Phần lớn chuyển tiếp cả khối và giao dịch. Nút có thể dùng một kết nối dự phòng đã xác minh để chuyển tiếp khối và mở kết nối thứ 11 trong thời gian ngắn để tìm nút khác. Tổng giới hạn là 125 kết nối. Nút nhận tối đa 117 kết nối đến, hoặc 115 khi có 10 kết nối đi. Ứng dụng trên máy tính hiện chỉ hiển thị tổng số nút đang kết nối. Mỗi thiết bị đào tự tạo khối. Nút trên máy tính chuyển tiếp các khối hoàn chỉnh và từ chối yêu cầu cấp việc đào cũng như kết quả tính toán do điện thoại gửi đến.

Khi khởi động lại, nút tiếp tục từ khối cuối cùng đã tự xác minh và kiểm tra các khối mới. Nếu bản ghi xác minh đã lưu bị thiếu hoặc không khớp, nút sẽ kiểm tra lại lịch sử đã lưu.

SUMUWW PC 0.57.61 · Nút xác thực, lưu trữ, truyền và cung cấp dữ liệu chuỗi.

## Mạng và địa chỉ

Mạng công khai là `sumuww`, bí danh nội bộ là `dora`. Kiểm tra hash khối khởi nguyên bên dưới. Địa chỉ gốc dùng witness v0 P2WPKH và HASH160 của khóa công khai secp256k1 nén. Không bắt buộc memo hay tag. Từ chối sai mạng và checksum không hợp lệ. Ghi lại nhánh HD nhận/tiền thừa và chỉ số; không giả định đường dẫn suy dẫn của Bitcoin.

## Xác thực và giới hạn

Chủ động bật RPC tại loopback dạng số `127.0.0.1:18443` với Bearer token riêng tư. Không cung cấp mở khóa ví hay ký từ xa. Dùng dịch vụ cục bộ hoặc đường hầm có xác thực; yêu cầu trình duyệt Origin/Referer bị từ chối. JSON-RPC dùng POST `/rpc`, `params` dạng đối tượng/mảng và `id`; thông báo trả HTTP 204. Giới hạn: thân 8004096 byte, header 8192, lô 16, yêu cầu đồng thời 16, hạn 10 giây; limit 1–1000, offset 0–1000000. Có 28 phương thức và 11 tuyến REST.

## Tra cứu giao dịch và khối

`getrawtransaction` tìm trong chuỗi hoạt động và mempool, không tìm giao dịch chỉ còn ở nhánh bị loại. Đầu vào chỉ ra đầu ra trước đó, không phải một địa chỉ người gửi duy nhất. `getblock` nhận `verbose` Boolean; khối lưu nhưng không hoạt động có `active=false`, `confirmations=-1`. Vẫn lấy được giao dịch thô qua hash khối. `findspendingtransaction` chỉ tìm khoản chi đã xác nhận trong chuỗi hoạt động; null không chứng minh khả dụng. Kiểm tra `gettxout` với `include_mempool=true`. Số xác nhận và trạng thái hoạt động có thể đổi sau tái tổ chức.

## Kiểm chứng

Cài các phụ thuộc rồi chạy python examples/node_contract.py từ mã nguồn. Khóa thử nghiệm công khai và regtest tạm thời kiểm tra gửi, từ chối, xác nhận, tái tổ chức và lưu giữ dữ liệu. Không dùng tiền thật, hồ sơ người dùng hoặc thiết bị ký phần cứng.

```text
network: sumuww (dora)
genesis: 00000032e243a8c71b449b13c2da733dd329f308a75aa4358f3f22707a28af97
HRP: sumuww
P2P magic: d052470c
1 SMW = 100000000 yugeon
```

[Tài liệu](README.html) · [Giao diện nút](EXCHANGE_INTEGRATION.html) · [API RPC và HTTP](RPC_API.html) · [Ghi chú phiên bản](RELEASE_NOTES.html) · [Kiểm chứng](EXCHANGE_EXAMPLES.html)

[Tài liệu chi tiết tiếng Anh](../../../EXCHANGE_INTEGRATION.html) · [API_CONTRACT.json](../../../API_CONTRACT.json) · [vectors.json](../../../examples/exchange/vectors.json)

<!-- payment-policy-20261116 -->

## Phí, giao dịch đã kiểm tra và khả năng tương thích

Phí bằng tổng giá trị đầu vào trừ tổng giá trị đầu ra. Ước tính chỉ tính đầu ra tiền thừa khi ví thực sự tạo khoản tiền thừa đạt ngưỡng quy định. Phần còn lại dưới ngưỡng được cộng vào phí; phí cuối cùng và tổng số tiền trừ khỏi ví được hiển thị để kiểm tra. Đơn vị mức phí là yugeon/vB. Kích thước ảo bằng trọng số giao dịch chia bốn rồi làm tròn lên.

Ví chỉ chọn đầu vào và đầu ra một lần, sau đó ký đúng phương án giao dịch đó. Khi bạn xác nhận, ví gửi giao dịch đã ký được lưu sẵn, không dựng lại giao dịch hay tính lại phí. Nếu báo phí hết hạn hoặc đầu vào đã được chi tiêu, bạn cần kiểm tra lại. Được chấp nhận vào hàng đợi cục bộ không có nghĩa là đã được xác nhận trong khối.

Với thanh toán P2WPKH thông thường, ví tạo chữ ký low-R và low-S dài tối đa 71 byte, bao gồm byte SIGHASH_ALL. Đây là chính sách ký và ước tính kích thước, không phải giới hạn đồng thuận mới đối với những chữ ký hợp lệ khác. Chữ ký ngắn hơn có thể làm kích thước ảo thực tế nhỏ hơn ước tính. 

<!-- /payment-policy-20261116 -->

Sau khi nhận được phản hồi phiên bản hợp lệ, nút dành thời gian cho nút bên kia gửi xác nhận. Nếu hai kết nối đi đến cùng một nút, một đường kết nối khả dụng được giữ cho đến khi một trong hai hoàn tất đồng bộ. 
