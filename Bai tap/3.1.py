import math

# Hàm tính tổ hợp (binomial coefficient)
def binomial_coefficient(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Tổng số máy
n = 5
# Xác suất một máy bị hỏng
p = 0.1

# Xác suất để có đúng 2 máy hỏng
k = 2
prob_2_machines_fail = binomial_coefficient(n, k) * (p**k) * ((1 - p)**(n - k))

# Xác suất để có không quá 2 máy hỏng
prob_up_to_2_machines_fail = 0
for k in range(0, 3):
    prob_up_to_2_machines_fail += binomial_coefficient(n, k) * (p**k) * ((1 - p)**(n - k))

print(f"Xác suất để trong một ngày có đúng 2 máy hỏng: {prob_2_machines_fail:.4f}")
print(f"Xác suất để trong một ngày có không quá 2 máy hỏng: {prob_up_to_2_machines_fail:.4f}")