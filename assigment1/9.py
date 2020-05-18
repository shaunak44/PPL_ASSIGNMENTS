n1 = int(input("Enter start number: "))
n2 = int(input("Enter end number: "))

for n in range(n1, n2):
    count = 0
    hm = 0
    for i in range(2, int(n/2) + 1):
        if not (n % i):
            hm += 1 / i
            count += 1
    hm += 1/ n + 1
    count += 2
    hm = count / hm
    hi = int(hm)
    if hi == hm:
        print(n,"is Harmonic Number")
