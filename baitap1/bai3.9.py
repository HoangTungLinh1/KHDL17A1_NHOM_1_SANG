def he_so_nhi_thuc(n, k):
    tuso = 1
    mauso = 1
    for i in range(n - k + 1, n + 1):
        tuso *= i
    for i in range(1, k + 1):
        mauso *= i
    return tuso // mauso
def xac_suat_nhi_thuc(n, p, k):
    return he_so_nhi_thuc(n, k) * (p ** k) * ((1 - p) ** (n - k))
so_sinh_vien = 650
xac_suat_den = 0.7
# 1
so_sinh_vien_toi_da = 440
xac_suat_1 = sum(xac_suat_nhi_thuc(so_sinh_vien, xac_suat_den, k) for k in range(so_sinh_vien_toi_da))
print(f"Xác suất số sinh viên đến đọc sách ít hơn 440 sinh viên: {xac_suat_1}")
#2
xac_suat_tong = 0
so_ghế = 0
while xac_suat_tong < 0.99:
    xac_suat_tong += xac_suat_nhi_thuc(so_sinh_vien, xac_suat_den, so_ghế)
    so_ghế += 1
print(f"Số ghế cần chuẩn bị để đảm bảo xác suất 0.99 có đủ chỗ cho sinh viên đến đọc sách: {so_ghế}")
