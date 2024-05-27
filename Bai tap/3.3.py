import math

# Hàm tính tổ hợp (binomial coefficient)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Thông số
n = 9  # Số lần lấy bi
p = 0.6  # Xác suất lấy được bi vàng
k = 4  # Số lần lấy được bi vàng

# Tính xác suất để có đúng 4 lần lấy được bi vàng
prob_4_vang = binomial_coefficient(n, k) * (p**k) * ((1 - p)**(n - k))

print(f"Xác suất để có đúng 4 lần lấy được bi vàng: {prob_4_vang:.4f}")



# Số lần chẵn trong 9 lần lấy (2, 4, 6, 8)
total_even_positions = 4
total_positions = 9
total_vang = 4  # Đã biết có 4 lần lấy được bi vàng

# Tính xác suất để 4 bi vàng nằm trong 4 lần chẵn
# Dùng công thức hypergeometric
prob_vang_in_even_positions = binomial_coefficient(total_even_positions, total_vang) / binomial_coefficient(total_positions, total_vang)

print(f"Xác suất để các bi vàng nằm ở các lần lấy chẵn: {prob_vang_in_even_positions:.4f}")