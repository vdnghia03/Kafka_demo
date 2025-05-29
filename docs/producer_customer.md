
# About Producer and Customer

---

## 🔁 Tổng quan hoạt động

> **“Các sự kiện (events) được tạo ra bởi producer và được đọc bởi consumer.”**

---

## 🏭 **Producer** là gì?

* **Producer** là "người tạo dữ liệu".
* Nó tạo ra các **sự kiện (event)** và gửi chúng vào **Kafka Topic**.
* Ví dụ: một trang web bán hàng tạo dữ liệu đơn hàng mỗi khi có người mua → đó là một event.

📌 Trong hình: Những khối nhỏ ghi “EVENT” là các dữ liệu mà producer gửi vào Kafka.

---

## 🗃️ **Kafka Topic** là gì?

* Đây là **nơi lưu trữ các sự kiện**, giống như một **hộp thư** hoặc **kênh truyền dữ liệu**.
* Các sự kiện trong topic được lưu **theo thứ tự** (ordered sequence).
* Nhiều consumer có thể cùng đọc dữ liệu từ đây mà **không làm ảnh hưởng đến nhau**.

📌 Trong hình: Hàng ô vuông thể hiện topic — các ô chứa các event xếp theo thứ tự.

---

## 👂 **Consumer** là gì?

* **Consumer** là "người đọc dữ liệu".
* Nó đọc dữ liệu từ Kafka topic **tùy theo tốc độ của riêng nó** (không bị ép đọc ngay lập tức).
* Ví dụ: một hệ thống phân tích dữ liệu đọc đơn hàng từ Kafka topic để vẽ biểu đồ.

📌 Trong hình: Consumer ở dưới đang đọc dữ liệu từ topic.

---

## 📬 **Mô hình publish-subscribe**

* **Producer**: "publish" (phát hành dữ liệu)
* **Consumer**: "subscribe" (đăng ký nhận dữ liệu)
* Nhiều consumer có thể đăng ký đọc cùng một topic, **không can thiệp lẫn nhau**.

📌 Mô hình này rất hiệu quả để **truyền thông tin theo thời gian thực** giữa các phần khác nhau của hệ thống.

---

## ✅ Tóm tắt dễ hiểu

| Thành phần        | Vai trò                                            | Ví dụ dễ hiểu                   |
| ----------------- | -------------------------------------------------- | ------------------------------- |
| Producer          | Tạo dữ liệu & gửi vào topic                        | Website gửi dữ liệu đơn hàng    |
| Kafka Topic       | Nơi lưu dữ liệu theo thứ tự                        | Một kênh chứa các đơn hàng      |
| Consumer          | Đọc dữ liệu từ topic                               | Phần mềm báo cáo đọc đơn hàng   |
| Publish-Subscribe | Cách truyền dữ liệu từ Producer đến nhiều Consumer | Giống như bạn gửi tin nhắn nhóm |

---

Slide này minh họa một ví dụ thực tế về việc sử dụng Kafka trong hệ thống xử lý đơn hàng. Dưới đây là phần giải thích **đơn giản và dễ hiểu**:

---

## 🎯 Chủ đề chính:

> Mô hình **producer - consumer** dùng trong việc xử lý đơn hàng (order event).

---

### 🔶 **Producer: `order_service`**

* Đây là dịch vụ **tạo ra sự kiện** khi có đơn hàng mới.
* Nó tạo một event có tên là `"order_placed"` (đã đặt hàng) và **gửi vào Kafka topic** có tên là `"orders topic"`.

📦 Ví dụ event gửi vào Kafka:

```json
{
  "event_type": "order_placed",
  "order_id": 301,
  "customer_id": 101,
  "total_amount": 2090.0,
  "timestamp": "2025-01-26T14:20:00Z"
}
```

---

### 🔽 **Kafka Topic: `orders topic`**

* Là "nơi chứa" tất cả các sự kiện về đơn hàng.
* Mỗi sự kiện sẽ được lưu lại theo thứ tự để các dịch vụ khác có thể **đọc lại khi cần**.

---

### 🟩 **Consumer: `inventory_service`**

* Đây là dịch vụ kiểm soát kho hàng.
* Nó **đăng ký lắng nghe (subscribe)** Kafka topic `"orders topic"`, đọc từng đơn hàng mới, và **cập nhật lại tồn kho**.

---

### 💡 Điểm quan trọng:

> **Producer và Consumer không cần biết nhau** — gọi là `decoupled` (tách rời).

* `order_service` chỉ gửi sự kiện.
* `inventory_service` chỉ cần biết có đơn hàng để cập nhật kho.
* Chúng hoạt động **độc lập** → dễ mở rộng và bảo trì hệ thống.

---

## ✅ Tóm tắt dễ hiểu:

| Thành phần          | Vai trò                                                         |
| ------------------- | --------------------------------------------------------------- |
| `order_service`     | Gửi event khi có đơn hàng mới vào Kafka (`producer`)            |
| `orders topic`      | Lưu trữ tất cả event dạng "order placed"                        |
| `inventory_service` | Đọc các đơn hàng từ topic và cập nhật tồn kho (`consumer`)      |
| `decoupled`         | Hai dịch vụ này không cần biết nhau nhưng vẫn phối hợp hiệu quả |

---

Slide này giải thích **cách hoạt động của partition (phân vùng)** trong Kafka topic — rất quan trọng để **Kafka xử lý nhanh và mở rộng tốt**.

---

## 📌 Tóm tắt slide:

> **Partitioning** cho phép **nhiều producer** và **nhiều consumer** hoạt động song song mà không bị xung đột.

---

## ✅ Giải thích từng phần:

### 1. **Topic được chia thành nhiều partition**

* Mỗi topic (chủ đề) không lưu dữ liệu trong một hàng duy nhất, mà được chia ra nhiều **partition** (P1, P2, P3, P4).
* Mỗi partition là một dãy dữ liệu riêng biệt, lưu trữ sự kiện theo **thứ tự xuất hiện**.

---

### 2. **Producer gửi sự kiện vào topic**

* `producer 1` và `producer 2` đều có thể gửi dữ liệu vào cùng một topic.
* **Kafka sẽ quyết định ghi sự kiện vào partition nào** trong topic.

---

### 3. 🔑 **Vai trò của `key`** (rất quan trọng):

* Mỗi sự kiện Kafka có thể có một **key** (khóa), ví dụ: `customer_id`, `order_id`...
* Kafka sử dụng `key` để **tính toán (hash)** và quyết định **partition nào sẽ lưu sự kiện**.

👉 **Nếu nhiều sự kiện có cùng key**, chúng **luôn được ghi vào cùng một partition**.

### 🔁 Tại sao điều này quan trọng?

* Để **đảm bảo thứ tự** các sự kiện có cùng key!
* Ví dụ: nếu bạn gửi các đơn hàng từ cùng một khách hàng, chúng cần đến đúng thứ tự → thì phải vào cùng một partition.

---

### 4. **Kafka đảm bảo thứ tự trong mỗi partition**

* **Chỉ trong 1 partition**, Kafka đảm bảo thứ tự **sự kiện ghi trước – đọc trước**.
* Nhưng giữa các partition khác nhau thì không có thứ tự chung.

---

## 🔄 Minh họa đơn giản:

| Event (đơn hàng)    | Key (`customer_id`) | Ghi vào Partition |
| ------------------- | ------------------- | ----------------- |
| Order #1 của KH 123 | 123                 | P1                |
| Order #2 của KH 123 | 123                 | P1                |
| Order của KH 456    | 456                 | P3                |

→ Hai đơn hàng của khách 123 luôn vào cùng partition P1 → giữ được **thứ tự xử lý**.

---

## ✅ Lợi ích của Partition + Key

* **Scale tốt**: nhiều producer & consumer cùng lúc.
* **Đảm bảo thứ tự** theo key (cực kỳ quan trọng với các app tài chính, giao dịch).
* **Phân tán dữ liệu** để xử lý nhanh hơn.

---

# Thuc hanh KafKa

- Buoc 1: Tao moi truong ao venv va setup moi truong: 
```bash
    uv venv
    source .venv/bin/activate
    uv pip install quixstream
    mkdir data
    mkdir src
```
Ben trong thu muc data chuan bi file jokes.json

- Buoc 2: Tao producer.py
+ Khoi chay docker
```bash
    docker compose up -d
```

+ Tao app
```python
  app = Application(broker_address = "localhost:9092", consumer_group = "text-splitter")
```

+ Tao topic
```python
jokes_topic = app.topic(name = "jokes", value_serializer = "json")
```

+ Mo file Jokes.json

+ Producer tao Message

+ Day Message vao Joke Topic

+ Vao container va kiem tra :
```bash

docker exec -it broker /bin/bash
kafka-topics --list --bootstrap-server localhost:9092
kafka-topics --describe --topic jokes --bootstrap-server localhost:9092

kafka-console-consumer --bootstrap-server localhost:9092 --topic jokes --from-beginning

```
  




