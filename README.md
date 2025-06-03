## KAFKA PRICE REALTIME


## INTRODUCTION

Project xây dựng nhằm demo một ứng dụng streamming sử dụng kafka lấy dữ liệu từ API. Producer liên tục cập nhật lấy dữ liệu mới nhất từ API sau mỗi 10s và Consumer sẽ lấy dữ liệu từ topic đó ngay sau khi producer gởi lên. Sau đó lưu trữ dữ liệu ấy vào postgresql. Ứng dụng streamlit kết nối đến postgresql lấy dữ liệu và trực quang biểu đồ để dễ nhìn.

## Overview

### Data:
- Sử dụng data từ API trong web Coin Market này ![Link](https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency). Bạn nên đăng kí một tài khoản miễn phí và vào dashboard của nó để lấy API
- Để tìm hiểu về data, hay đọc qua file [Exploratory Data Analysis](/exploration/coins_eda.ipynb)


### Architecture:
![ETL](/docs/streaming_coin_data.png)

Trong đó:
- **Kafka**: Streaming data từ API coin market
- **Postgres**: Là cơ sở dữ liệu, lưu trữ các giá trị mới nhất có được từ kafka consumer
- **Streamlit**: Trực quan dashboard

## Prequisite
1. [Docker](https://www.docker.com/)
2. [Git](https://git-scm.com/)


## Set up
1. Đầu tiên ta clone git repo này về local bằng `git clone`
2. Tạo file `.env` có nội dung giống với [env.template](env.template)
   - Lưu ý là API KEY lấy từ ![Link](https://coinmarketcap.com/api/documentation/v1/#tag/cryptocurrency)
3. Tạo môi trường ảo: Nên tải môi trường uv: *pipx install uv*

```bash
    # Tạo môi trường ảo
    uv venv
    # Kích hoạt môi trường ảo
    source .venv/bin/activate

    # Tải các gói vào môi trường ảo
    uv pip install quixtreams psycopg-binary duckdb pandas matplotlib streamlit streamlit_autorefresh 

```

4. Chạy docker compose
```bash
    # Build các image
    make build # Tương đường docker compose build

    # Chạy container từ image
    make up # Tương đương docker compose up -d

    # Để xóa container và dừng lại thì dùng 
    make down # Tương đương docker compose down

```
- Lưu ý là khi dùng Linux/Ubuntu sẽ gặp các lỗi phân quyền liên quan đến các file và thư mục, nên tra chatgpt để fix lỗi

5. Chạy file producer và consumer
- Sử dụng terminal hiện chaỵ
```bash
    python3 src/coin_api_streamming/coin_producer.py

```

- Bật thêm một terminal mới, kích hoạt môi trường ảo và chạy
```bash
    python3 src/coin_api_streamming/coin_consumer.py
```

6. Chạy Ứng dụng streamlit
- Bật terminal mới và môi kích hoạt môi trường ảo và chạy
```bash
    streamlit run src/coin_api_streaming/dashboard.py
```

## Visualize streamlit

![GIF](/docs/Streamlit1.gif)


## Future Update
- Thêm orchestrator Dagster để tạo luồng tự động
- Suy nghĩ về việc sử dụng DBT cho việc transform data
- Suy nghĩ về các ứng dụng ML Realtime

## Conclusion

Project hướng dẫn xây dựng Kafka cơ bản đơn giản để tìm hiểu.
