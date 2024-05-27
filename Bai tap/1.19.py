
P_H1 = 2 / 5
P_H2 = 1 / 5
P_H3 = 2 / 5
P_A_given_H1 = 0.70
P_A_given_H2 = 0.75
P_A_given_H3 = 0.50
P_A = P_A_given_H1 * P_H1 + P_A_given_H2 * P_H2 + P_A_given_H3 * P_H3
P_H1_given_A = (P_A_given_H1 * P_H1) / P_A

print(f"Xác suất để sản phẩm loại A được mua ở cửa hàng I là: {P_H1_given_A:.4f}")