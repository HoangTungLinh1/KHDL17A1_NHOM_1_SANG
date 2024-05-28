import math

def he_so_nhi_thuc(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def xac_suat_nhi_thuc(n, p, k):
    he_so = he_so_nhi_thuc(n, k)
    xac_suat = he_so * (p**k) * ((1 - p)**(n - k))
    return xac_suat

tong_so_lan_thu = 14 + 9 + 7
xac_suat_thanh_cong = 0.1
so_lan_thanh_cong = 4

xac_suat = xac_suat_nhi_thuc(tong_so_lan_thu, xac_suat_thanh_cong, so_lan_thanh_cong)
print(xac_suat)
