number = [2, 4, 5, 6, 12, 16, 17, 20, 21]
j = 0
for i in range(1, 25) :
    if( i != number[j]) :
        print(i)
    elif(i == number[j] and j < 8) :
        j = j + 1

