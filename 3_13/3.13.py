import math
lambada=2
#a)
def xac_suat_poisson(n,k):
  return ((n**k)*(math.exp(-n)))/(math.factorial(k))
#xác suất tất cả 4 ô tô đều được thuê
all_hire = xac_suat_poisson(lambada,4)
print("Xác suất tất cả 4 ô tô đều được thuê:",all_hire)
#Xác suất không phải tất cả 4 ô tô đều được thuê
not_all_hire = 1 - all_hire
print("Xác suất ko phải thuê 4 xe là:",not_all_hire)
#Xác suất cửa hàng không đáp ứng yêu cầu
probability_unsatisfied = 1-sum(xac_suat_poisson(lambada,i) for i in range(5))
print("Xác suất cửa hàng ko đáp ứng dc yêu cầu:",probability_unsatisfied)
###
cars_rented = lambada
print("TRung bình số ô tô được thuê:",cars_rented)
##
k = 4
xac_suat = 1
while xac_suat>=0.02:
  xac_suat=1-sum(xac_suat_poisson(lambada,i) for i in range(k+1))
  if xac_suat<0.02:
    break
  k+=1
print(f'Cửa hàng cần có ít nhất {k} ô tô để xác suất không đáp ứng được nhu cầu thuê xe bé hơn 2%')
