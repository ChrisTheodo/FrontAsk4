import time
start_time = time.time()

digit = int(input("digit:"))
fibonacci = [0,1]
sameNum = []
isPrime = True

while digit > len(sameNum)-1:
    num = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(num)

    for i in range(2, int(num/2)+1):
        if num % i == 0:
            isPrime = False
            break
        else:
            isPrime = True
    
    if isPrime == True:
        sameNum.append(num) 

if digit == len(sameNum)-1:
    print(f"to {digit}o pfhfio einai to {sameNum[-1]}")




    







print("time elapsed:", time.time() - start_time, "seconds")
