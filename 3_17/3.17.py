#1
#Giá trị trung bình u
u =2 # Giả sử u=2
#Độ lệch chuẩn 
sigma = 0.01*2**2
#Chiều dài xe hơi cao cấp lơn hơn 15% chiều dài trung bình xe
cars_lenth = 1.15*u
#Tính z
z= (cars_lenth-u)/(sigma)
p= 1-0.9335
print(f"Tỉ lệ chỗ đậu xe mà người đàn ông có thể sử dụng là: {p:.4f} hoặc {p * 100:.2f}%")
#2
# Giá trị trung bình u
u = 4
# Độ lệch chuẩn 
sigma = u * 0.1
# Tính z-score cho xác suất tích lũy 90%
z_score = 1.3
# Tính chiều dài xe X sử dụng công thức chuyển đổi từ z
X = z_score * sigma + u
print(f"Chiều dài xe để sử dụng 90% chỗ đậu xe là: {X:.3f} m")