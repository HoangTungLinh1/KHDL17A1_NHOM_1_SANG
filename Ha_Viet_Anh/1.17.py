# Tỷ lệ các cặp sinh đôi theo giới tính
P_TT = 0.34
P_GG = 0.30
P_TG_GT = 0.36

# Xác suất cặp sinh đôi giả (P(G)) từ tỷ lệ TG/GT
P_G = P_TG_GT / 0.5

# Xác suất cặp sinh đôi thật (P(T))
P_T = 1 - P_G

print(f"Tỷ lệ cặp sinh đôi thật: {P_T:.2%}")

# Tỷ lệ cặp sinh đôi thật trong số các cặp sinh đôi có cùng giới tính (TT hoặc GG)
P_same_sex_given_T = 1  # Cặp sinh đôi thật luôn cùng giới tính
P_same_sex_given_G = 0.25 + 0.25  # TT hoặc GG trong cặp sinh đôi giả

# Tỷ lệ các cặp sinh đôi có cùng giới tính (TT hoặc GG)
P_same_sex = P_TT + P_GG

# Tỷ lệ cặp sinh đôi thật trong số các cặp sinh đôi có cùng giới tính
P_T_given_same_sex = (P_T * P_same_sex_given_T) / P_same_sex

print(f"Tỷ lệ cặp sinh đôi thật trong số các cặp sinh đôi có cùng giới tính: {P_T_given_same_sex:.2%}")