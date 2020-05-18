n1 = int(input("Enter start number: "))
n2 = int(input("Enter last number: "))

for n in range(n1, n2):
    s = 0
    count = 0
    tmp = n
    while tmp > 0:
        digit = tmp % 10
        s += digit ** 3
        tmp //= 10
    if n == s:
       print(n, "is an Armstrong Number")
