import random
number=random.randint(1,100)
print("guessing the number")
print(number)
for i in range(1,100):
    
    print("if the guess is correct enter 0 f your no. is less than the given number enter -1 else enter 1")
    num=int(input("enter your choice:"))
    if (num==0):
        result="number is correct"
        break
    elif(num==-1):
        result=random.randint(1,number-1)
    else:
        result=random.randint(number+1,100)
    print(result)
    