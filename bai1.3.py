def trinh_tu_tung(chuoi_hien_tai, do_sau_max, kq):
    if chuoi_hien_tai and chuoi_hien_tai[-1] == 6:
        kq.append(chuoi_hien_tai)
        return
    
    if len(chuoi_hien_tai) >= do_sau_max:
        return
    
    for i in range(1, 7):
        trinh_tu_tung(chuoi_hien_tai + [i], do_sau_max, kq)

def khong_gian_mau(do_sau_max=10):
    kq = []
    trinh_tu_tung([], do_sau_max, kq)
    return kq

khong_gian = khong_gian_mau(5)  
for chuoi in khong_gian:
    print(chuoi)

def tung_khong_gian_mau(so_lan_tung_max=10):
    return list(range(1, so_lan_tung_max + 1))
khong_gian_tung = tung_khong_gian_mau(10)  
print(khong_gian_tung)