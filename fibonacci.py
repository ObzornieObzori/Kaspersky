def f(n,k):
  if n==1 or n==2: return 1
  else: return f(n-1, k)+f(n-2, k) * k
print(f(int(input("Введите N: ")),int(input('Введите K: '))))
