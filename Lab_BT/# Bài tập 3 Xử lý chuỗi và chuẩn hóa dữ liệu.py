# Bài tập 3: Xử lý chuỗi và chuẩn hóa dữ liệu

# Nhập họ tên
ho_ten = input("Nhập họ tên: ")

# Nhập năm sinh
nam_sinh = input("Nhập năm sinh: ")

# Tách họ tên và lấy tên cuối cùng
ten = ho_ten.split()[-1]

# Lấy 3 ký tự đầu và viết hoa
ten_viet_hoa = ten[0:3].upper()

# Tạo mã ưu đãi bằng F-string
ma_uu_dai = f"{ten_viet_hoa}-{nam_sinh}-VIP"

# In kết quả
print("Mã ưu đãi:", ma_uu_dai)