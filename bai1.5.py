def co_dung_mot_hs_dat(B1, B2, B3, B4):
    return (B1 and not B2 and not B3 and not B4) or \
           (not B1 and B2 and not B3 and not B4) or \
           (not B1 and not B2 and B3 and not B4) or \
           (not B1 and not B2 and not B3 and B4)

def co_dung_ba_hs_dat(B1, B2, B3, B4):
    return (B1 and B2 and B3 and not B4) or \
           (B1 and B2 and not B3 and B4) or \
           (B1 and not B2 and B3 and B4) or \
           (not B1 and B2 and B3 and B4)

def co_it_nhat_mot_hs_dat(B1, B2, B3, B4):
    return B1 or B2 or B3 or B4

def khong_hs_dat(B1, B2, B3, B4):
    return not B1 and not B2 and not B3 and not B4

# Kiểm tra tất cả các tổ hợp có thể của B1, B2, B3 và B4
for B1 in [True, False]:
    for B2 in [True, False]:
        for B3 in [True, False]:
            for B4 in [True, False]:
                print(f"\nB1={B1}, B2={B2}, B3={B3}, B4={B4}")
                if co_dung_mot_hs_dat(B1, B2, B3, B4):
                    print("Có đúng một sinh viên đạt yêu cầu:", co_dung_mot_hs_dat(B1, B2, B3, B4))
                    print("(B1 ∧ -B2 ∧ -B3 ∧ -B4) ∨ (-B1 ∧ B2 ∧ -B3 ∧ -B4) ∨ (-B1 ∧ -B2 ∧ B3 ∧ -B4) ∨ (-B1 ∧ -B2 ∧ -B3 ∧ B4)")
                else:
                    print("Có đúng một sinh viên đạt yêu cầu:", co_dung_mot_hs_dat(B1, B2, B3, B4))
                if co_dung_ba_hs_dat(B1, B2, B3, B4):
                    print("Có đúng ba sinh viên đạt yêu cầu:", co_dung_ba_hs_dat(B1, B2, B3, B4))
                    print("(B1 ∧ B2 ∧ B3 ∧ -B4) ∨ (B1 ∧ B2 ∧ -B3 ∧ B4) ∨ (B1 ∧ -B2 ∧ B3 ∧ B4) ∨ (-B1 ∧ B2 ∧ B3 ∧ B4)")
                else:
                    print("Có đúng ba sinh viên đạt yêu cầu:", co_dung_ba_hs_dat(B1, B2, B3, B4))
                if co_it_nhat_mot_hs_dat(B1, B2, B3, B4):
                    print("Có ít nhất một sinh viên đạt yêu cầu:", co_it_nhat_mot_hs_dat(B1, B2, B3, B4))
                    print("B1 ∨ B2 ∨ B3 ∨ B4")
                else:
                    print("Có ít nhất một sinh viên đạt yêu cầu:", co_it_nhat_mot_hs_dat(B1, B2, B3, B4))
                if khong_hs_dat(B1, B2, B3, B4):
                    print("Không có sinh viên nào đạt yêu cầu:", khong_hs_dat(B1, B2, B3, B4))
                    print("-B1 ∧ -B2 ∧ -B3 ∧ -B4")
                else:
                    print("Không có sinh viên nào đạt yêu cầu:", khong_hs_dat(B1, B2, B3, B4))