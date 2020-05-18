i, count  = 2, 0
amicables = []

print("Sr   First Number    Second Number")

while count < 10:
    div_sum1 = 0
    div_sum2 = 0
    
    for j in range(2, int(i ** 0.5)+1):
        if not (i % j):
            div_sum1 += (j + i/j)
    div_sum1 += 1
    
    if (div_sum1 != i) and ([div_sum1, i] not in amicables):
        for j in range(2, int((div_sum1 ** 0.5)+1)):
            if not (div_sum1 % j):
                div_sum2 += (j + div_sum1/j)
        div_sum2 += 1
        
        if (div_sum2 == i):
            amicables.append([i, int(div_sum1)])
            print(count,"\t",i,"\t\t",int(div_sum1))
            count += 1
    i += 1
