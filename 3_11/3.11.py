def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)
def nCr(n,r):
  return factorial(n)//(factorial(n)*factorial(n-r))
def xac_suat(n,p,k):
  return nCr(n,k)*(p**k)*(1-p)**(n-k)
#Creative table
def creative_table(n1,p1,n2,p2):
    X_plus_Y = {}
    for k1 in range(0,n1+1):
        for k2 in range(0,n2+1):
            k=k1+k2
            mun = xac_suat(n1,p1,k1)*xac_suat(n2,p2,k2)
            if k in X_plus_Y:
                X_plus_Y[k]+=mun
            else:
                X_plus_Y[k]=mun
    return X_plus_Y
dis = creative_table(1,0.2,2,0.2)
print("Phân phối xác suất của X+Y khi X~B(1;1/5) và Y~B(2;1/5):")
for k,mun in dis.items():
    print(f"X+Y={k}: {mun:.5f}")