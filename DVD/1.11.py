def chon_it_nhat_1_trong_3_tieu_chi(P_A, P_B, P_C, P_A_hop_B_hop_C):
    P_none = 1 - P_A_hop_B_hop_C
    return 1 - P_none

def khong_chon_tieu_chi_nao(P_A_hop_B_hop_C):
    return 1 - P_A_hop_B_hop_C

def chi_chon_dieu_hoa_nhiet_do(P_C, P_A_hop_B, P_A_hop_C, P_B_hop_C):
    P_chon_C = P_C - P_A_hop_C - P_B_hop_C + P_A_hop_B
    return P_chon_C

def chon_chinh_xac_1_trong_3_tieu_chi(P_A, P_B, P_C, P_A_hop_B, P_A_hop_C, P_B_hop_C, P_A_hop_B_hop_C):
    P_chon_A = P_A - P_A_hop_B - P_A_hop_C + P_A_hop_B_hop_C
    P_chon_B = P_B - P_A_hop_B - P_B_hop_C + P_A_hop_B_hop_C
    P_chon_C = P_C - P_A_hop_C - P_B_hop_C + P_A_hop_B_hop_C
    return P_chon_A + P_chon_B + P_chon_C

P_A = 0.7
P_B = 0.75
P_C = 0.8
P_A_hop_B = 0.8
P_A_hop_C = 0.85
P_B_hop_C = 0.9
P_A_hop_B_hop_C = 0.95

P_chon_it_nhat_1_tieu_chi = chon_it_nhat_1_trong_3_tieu_chi(P_A, P_B, P_C, P_A_hop_B_hop_C)
P_khong_chon_tieu_chi_nao = khong_chon_tieu_chi_nao(P_A_hop_B_hop_C)
P_chi_chon_dieu_hoa_nhiet_do = chi_chon_dieu_hoa_nhiet_do(P_C, P_A_hop_B, P_A_hop_C, P_B_hop_C)
P_chon_chinh_xac_1_trong_3_tieu_chi = chon_chinh_xac_1_trong_3_tieu_chi(P_A, P_B, P_C, P_A_hop_B, P_A_hop_C, P_B_hop_C, P_A_hop_B_hop_C)

print(f"1) Xac suat chon it nhat 1 tieu chi trong 3 tieu chi: {P_chon_it_nhat_1_tieu_chi:.5f}")
print(f"2) Xac suat khong chon tieu chi nao: {P_khong_chon_tieu_chi_nao:.5f}")
print(f"3) Xac suat chi chon dieu hoa nhiet do: {P_chi_chon_dieu_hoa_nhiet_do:.5f}")
print(f"4) Xac suat chon chinh xac 1 trong 3 tieu chi tren: {P_chon_chinh_xac_1_trong_3_tieu_chi:.5f}")

