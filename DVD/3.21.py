import math
def tinh_toan_phuong_sai_va_do_lech_chuan(lambda_bai_cho):


    gia_tri = lambda_bai_cho / (lambda_bai_cho + 1)

    gia_tri_binh_phuong = lambda_bai_cho / (lambda_bai_cho + 2)

    phuong_sai = gia_tri_binh_phuong - (gia_tri ** 2)

    do_lech_chuan = math.sqrt(phuong_sai)
    return phuong_sai, do_lech_chuan

lambda_bai_cho = 2
phuong_sai, do_lech_chuan = tinh_toan_phuong_sai_va_do_lech_chuan(lambda_bai_cho)
print(f"Giá trị phương sai là : {phuong_sai}")
print(f"Giá trị độ lệch chuẩn là : {do_lech_chuan}")
