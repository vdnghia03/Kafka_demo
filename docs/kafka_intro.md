
## 🧠 Giả sử Kafka là... một **bưu điện hiện đại**

### Bạn có:

* 📬 **Kafka Broker** = Nhân viên bưu điện: nhận, lưu và gửi thư (dữ liệu).
* 📦 Các “bức thư” là dữ liệu mà hệ thống của bạn đang gửi đi.

---

## 🔍 **Schema Registry** là gì?

### 👉 Hãy tưởng tượng:

* Mỗi bức thư bạn gửi đều phải theo **một mẫu đơn nhất định**: có tên người nhận, địa chỉ, nội dung...
* Nếu **người gửi ghi sai mẫu**, người nhận sẽ **không hiểu hoặc hiểu sai**.

🎯 **Schema Registry** giống như một **kho lưu trữ mẫu thư**.

* Nó giúp đảm bảo **dữ liệu gửi đi luôn đúng định dạng**.
* Nếu ai đó muốn thay đổi mẫu thư (ví dụ thêm số điện thoại), Schema Registry **kiểm tra** để đảm bảo người nhận vẫn hiểu.

📌 Nói cách khác: Schema Registry = "cảnh sát định dạng dữ liệu".

---

## 📊 **Control Center** là gì?

### 👉 Giả sử:

* Bạn là người **quản lý bưu điện**. Bạn muốn:

  * Biết ai đang gửi nhiều thư.
  * Có bao nhiêu thư đang được xử lý.
  * Có ai gửi nhầm hay lỗi không?

🎯 **Control Center** giống như **bảng điều khiển giám sát**.

* Nó cho bạn thấy **Kafka đang hoạt động thế nào**.
* Có bao nhiêu dữ liệu đang đi qua.
* Dịch vụ nào đang chạy, có bị lỗi hay không.

📌 Nói cách khác: Control Center = "mắt thần" giám sát Kafka.

---

## Tóm tắt ngắn gọn

| Thành phần         | Vai trò đơn giản                           |
| ------------------ | ------------------------------------------ |
| 📨 Kafka Broker    | Gửi – Nhận – Lưu dữ liệu (như gửi thư)     |
| 📋 Schema Registry | Kiểm tra định dạng dữ liệu (giống mẫu thư) |
| 📊 Control Center  | Giao diện theo dõi mọi hoạt động           |

---

## Chạy KAFKA

### Bước 1: Chạy container: 
```bash
    docker compose up -d
```

### Bước 2: Vào bên trong container
```bash
    docker ps
    docker exec -it broker /bin/bash
```

### Buớc 3: Xem topic hiện có trong kafka container
```bash
    kafka-topics --list --bootstrap-server localhost:9092
```

### Buớc 4: Xem UI - Là từ control center cổng 9021
```bash
    localhost:9021
```