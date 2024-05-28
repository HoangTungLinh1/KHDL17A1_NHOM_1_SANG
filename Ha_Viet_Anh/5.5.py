import math

# Xác suất chậm tàu của mỗi hành khách
p = 0.007

# Số lượng hành khách
n = 20000

# Trung bình và độ lệch chuẩn của phân phối nhị thức
mu = n * p
sigma = math.sqrt(n * p * (1 - p))

# Giá trị của k
k = (180 - mu) / sigma

# Áp dụng bất đẳng thức Chebyshev để ước lượng xác suất
prob = 1 / (k ** 2)

print(f"Xác suất để có từ 100 đến 180 hành khách chậm tàu là ít hơn {prob:.4f}")