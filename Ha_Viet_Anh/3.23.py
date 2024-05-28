import math
import scipy.stats as stats

# Hàm tính xác suất cho phân phối chuẩn
def prob_normal(mu, sigma):
    return stats.norm.cdf(3) - stats.norm.cdf(-3)

# Hàm tính xác suất cho phân phối đều
def prob_uniform(a, b):
    sigma_uniform = (b - a) / (2 * math.sqrt(3))
    return stats.norm.cdf(3 * sigma_uniform) - stats.norm.cdf(-3 * sigma_uniform)

# Hàm tính xác suất cho phân phối Poisson
def prob_poisson(lambda_param):
    mu_poisson = lambda_param
    sigma_poisson = math.sqrt(lambda_param)
    return stats.norm.cdf(3 * sigma_poisson) - stats.norm.cdf(-3 * sigma_poisson)

# Trường hợp 1: Phân phối chuẩn
mu_normal = 0
sigma_normal = 1
print("Xác suất cho phân phối chuẩn:", prob_normal(mu_normal, sigma_normal))

# Trường hợp 2: Phân phối đều trên đoạn [-1; 1]
a_uniform = -1
b_uniform = 1
print("Xác suất cho phân phối đều:", prob_uniform(a_uniform, b_uniform))

# Trường hợp 3: Phân phối Poisson với tham số lambda = 0.09
lambda_poisson = 0.09
print("Xác suất cho phân phối Poisson:", prob_poisson(lambda_poisson))