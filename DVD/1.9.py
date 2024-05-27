def trung_thau_it_nhat_1_du_an(P_A, P_B, P_A_and_B):
    P_A_or_B = P_A + P_B - P_A_and_B
    return P_A_or_B

def trung_dung_1_du_an(P_A, P_B, P_A_and_B):
    P_only_A = P_A - P_A_and_B
    P_only_B = P_B - P_A_and_B
    return P_only_A + P_only_B

def trung_du_an_2_khi_biet_trung_du_an_1(P_A, P_A_and_B):
    return P_A_and_B / P_A

def trung_du_an_2_khi_biet_0_trung_du_an_1(P_A, P_B, P_A_and_B):
    P_not_A = 1 - P_A
    P_not_A_and_B = P_B - P_A_and_B
    return P_not_A_and_B / P_not_A

P_A = 0.5 # Xac suat trung thau du an 1
P_B = 0.4 # Xac suat trung thau du an 2
P_A_and_B = 0.1 # Xac suat trung thau ca 1 va 2

xac_suat_trung_it_nhat_1_du_an = trung_thau_it_nhat_1_du_an(P_A, P_B, P_A_and_B)
xac_suat_trung_dung_1_du_an = trung_dung_1_du_an(P_A, P_B, P_A_and_B)
xac_suat_trung_du_an_2_khi_biet_trung_du_an_1 = trung_du_an_2_khi_biet_trung_du_an_1(P_A, P_A_and_B)
xac_suat_trung_du_an_2_khi_biet_0_trung_du_an_1 = trung_du_an_2_khi_biet_0_trung_du_an_1(P_A, P_B, P_A_and_B)

print(f"1) Xac suat khi trung it nhat 1 du an: {xac_suat_trung_it_nhat_1_du_an:.5f}")
print(f"2) Xac suat khi trung dung 1 du an: {xac_suat_trung_dung_1_du_an:.5f}")
print(f"3) Xac suat khi trung du an 2 khi biet trung du an 1: {xac_suat_trung_du_an_2_khi_biet_trung_du_an_1:.5f}")
print(f"4) Xac suat khi trung du an 2 khi khong biet trung du an 1: {xac_suat_trung_du_an_2_khi_biet_0_trung_du_an_1:.5f}")
