

def isPerfectSquare(number):
    isPS=False
    sqrt=None
    
    for i in range(1,int(number/2)+2):
        if number==i*i:
            isPS = True
            sqrt = i
            break
        elif i*i>number:
            break

    return isPS,sqrt




number = 10
check,sqrt = isPerfectSquare(number)
print("Is {} a perfect square ? {} and it's square root is {}".format(number,check,sqrt))
