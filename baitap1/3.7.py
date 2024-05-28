import math

def he_so_nhi_thuc(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def xac_suat_nhi_thuc(n, p, k):
    he_so = he_so_nhi_thuc(n, k)
    xac_suat = he_so * (p**k) * ((1 - p)**(n - k))
    return xac_suat

tong_so_lan_thu = 300
xac_suat_be_trai = 0.48
#1
so_be_trai_1 = 180
xac_suat_1 = xac_suat_nhi_thuc(tong_so_lan_thu, xac_suat_be_trai, so_be_trai_1)
print(f"Xác suất có 180 bé trai: {xac_suat_1}")
#2
so_be_trai_bat_dau = 150
so_be_trai_ket_thuc = 170
xac_suat_2 = sum(xac_suat_nhi_thuc(tong_so_lan_thu, xac_suat_be_trai, k) for k in range(so_be_trai_bat_dau, so_be_trai_ket_thuc + 1))
print(f"Xác suất số bé trai sinh ra khoảng từ 150 đến 170: {xac_suat_2}")
#3
so_be_trai_3 = 169
xac_suat_3 = sum(xac_suat_nhi_thuc(tong_so_lan_thu, xac_suat_be_trai, k) for k in range(so_be_trai_3 + 1))
print(f"Xác suất số bé trai sinh ra ít hơn 170: {xac_suat_3}")
ROOT_KHDL17A1HN_Duong_Thanh_Chung_23174600048