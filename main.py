import streamlit as st
import pandas as pd
import numpy as np

# Tiêu đề của ứng dụng
st.title('Map')

# Tạo dữ liệu ngẫu nhiên cho tọa độ (latitude, longitude)
locate_map = pd.DataFrame(
    np.random.randn(50, 2) / [10, 10] + [15.4589, 75.0078],
    columns=['latitude', 'longitude']  # Đảm bảo tên cột chính xác
)

# Hiển thị bản đồ với tọa độ từ locate_map
st.map(locate_map)  # Sử dụng locate_map thay vì locate_app

