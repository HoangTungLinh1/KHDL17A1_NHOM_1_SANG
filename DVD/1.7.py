import math
def comb(n, k):
    return math.comb(n, k)
tong_so_nguoi = 10
men = 6
women = 4
so_nguoi_chon = 6
tong_so_cach_chon = comb(tong_so_nguoi, so_nguoi_chon)
#1) Chọn 4 nam
cach_chon_all_men = comb(men, so_nguoi_chon)
xac_suat_all_men = cach_chon_all_men / tong_so_cach_chon
#2) Chọn 4 nam 2 nữ
cach_chon_4_men_2_women = comb(men, 4) * comb(women, 2)
xac_suat_chon_4_men_2_women = cach_chon_4_men_2_women / tong_so_cach_chon
#3) Chọn ít nhất 2 nữ
cach_chon_0_women = comb(men, so_nguoi_chon)
cach_chon_1_woman = comb(men, 5) * comb(women, 1)
cach_chon_it_nhat_2_women = tong_so_cach_chon - (cach_chon_0_women + cach_chon_1_woman)
xac_suat_it_nhat_2_women = cach_chon_it_nhat_2_women / tong_so_cach_chon
print(f"1) Xác suất chọn 4 nam: {xac_suat_all_men:.5f}")
print(f"2) Xác suất chọn 4 nam và 2 nữ : {xac_suat_chon_4_men_2_women:.5f}")
print(f"3) Xác suất chọn ít nhất 2 nữ : {xac_suat_it_nhat_2_women:.5f}")

