so_xuc_xac1 = ['1', '2', '3', '4', '5', '6']
so_xuc_xac2 = ['1', '2', '3', '4', '5', '6']
khong_gian_bien_so_cap = []

for x in so_xuc_xac1:
    for y in so_xuc_xac2:
        khong_gian_bien_so_cap.append((x, y))
print('không gian biến sơ cấp là:',khong_gian_bien_so_cap)

tong_so_cham_bang_7 = 0
for x, y in khong_gian_bien_so_cap:
    if int(x) + int(y) == 7:
        tong_so_cham_bang_7 += 1

xac_suat = tong_so_cham_bang_7 / len(khong_gian_bien_so_cap)
print("Xác suất tổng số chấm là 7 khi lắc hai xúc xắc là:", xac_suat)
