# Bài tập 2: Máy phát sinh Mã ưu đãi

# Nhập họ tên
ho_ten = input("Nhập họ tên: ")

# Nhập năm sinh
nam_sinh = input("Nhập năm sinh: ")

# Xóa khoảng trắng và lấy 3 ký tự đầu tiên
ten_viet_hoa = ho_ten.replace(" ", "").upper()
ba_ky_tu_dau = ten_viet_hoa[0:3]

# Tạo mã ưu đãi
ma_uu_dai = ba_ky_tu_dau + "-" + nam_sinh + "-VIP"

# In kết quả
print("Mã ưu đãi:", ma_uu_dai)