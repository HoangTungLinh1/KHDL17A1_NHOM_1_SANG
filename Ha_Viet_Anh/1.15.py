# Xác suất lấy bi đỏ và bi trắng từ hộp 1
P_bi_do_tu_hop1 = 5 / 20
P_bi_trang_tu_hop1 = 15 / 20

# Xác suất lấy bi đỏ từ hộp 2 nếu bi đỏ được thêm vào hộp 2
P_bi_do_tu_hop2_khi_bi_do_duoc_them = 7 / 16
P_bi_trang_tu_hop2_khi_bi_do_duoc_them = 9 / 16

# Xác suất lấy bi đỏ từ hộp 2 nếu bi trắng được thêm vào hộp 2
P_bi_do_tu_hop2_khi_bi_trang_duoc_them = 6 / 16
P_bi_trang_tu_hop2_khi_bi_trang_duoc_them = 10 / 16

# Tính xác suất lấy bi đỏ từ hộp 2
P_bi_do_tu_hop2 = (P_bi_do_tu_hop1 * P_bi_do_tu_hop2_khi_bi_do_duoc_them +
                   P_bi_trang_tu_hop1 * P_bi_do_tu_hop2_khi_bi_trang_duoc_them)

# Tính xác suất lấy bi trắng từ hộp 2
P_bi_trang_tu_hop2 = (P_bi_do_tu_hop1 * P_bi_trang_tu_hop2_khi_bi_do_duoc_them +
                      P_bi_trang_tu_hop1 * P_bi_trang_tu_hop2_khi_bi_trang_duoc_them)

print(f"Xác suất nhận được bi đỏ: {P_bi_do_tu_hop2:.4f}")
print(f"Xác suất nhận được bi trắng: {P_bi_trang_tu_hop2:.4f}")