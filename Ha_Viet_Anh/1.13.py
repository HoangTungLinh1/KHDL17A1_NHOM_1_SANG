# Xác suất bắn trúng mục tiêu của mỗi khẩu pháo
P_A = 0.4
P_B = 0.7
P_C = 0.8

# Tính xác suất trúng mục tiêu k lần (k = 0, 1, 2, 3)
P_0_trung = (1 - P_A) * (1 - P_B) * (1 - P_C)
P_1_trung = P_A * (1 - P_B) * (1 - P_C) + (1 - P_A) * P_B * (1 - P_C) + (1 - P_A) * (1 - P_B) * P_C
P_2_trung = P_A * P_B * (1 - P_C) + P_A * (1 - P_B) * P_C + (1 - P_A) * P_B * P_C
P_3_trung = P_A * P_B * P_C

# Xác suất tiêu diệt mục tiêu khi trúng k phát đạn
P_tieu_diet_khi_1_trung = 0.3
P_tieu_diet_khi_2_trung = 0.7
P_tieu_diet_khi_3_trung = 1.0

# Tính xác suất tổng thể tiêu diệt mục tiêu
P_tieu_diet = (P_1_trung * P_tieu_diet_khi_1_trung + 
               P_2_trung * P_tieu_diet_khi_2_trung + 
               P_3_trung * P_tieu_diet_khi_3_trung)

print(f"Xác suất mục tiêu bị tiêu diệt: {P_tieu_diet:.4f}")

# Tính xác suất cả 3 khẩu pháo cùng bắn trúng mục tiêu khi mục tiêu đã bị tiêu diệt
P_ca_3_trung_khi_tieu_diet = P_3_trung / P_tieu_diet

print(f"Xác suất cả 3 khẩu pháo cùng bắn trúng mục tiêu khi mục tiêu đã bị tiêu diệt: {P_ca_3_trung_khi_tieu_diet:.4f}")