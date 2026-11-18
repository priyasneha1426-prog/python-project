try:
    num=int(input("Enter the number : "))
    result=10/num
except ValueError:
    print("That's not a valid number")
except ZeroDivisionError:
    print("Cannot divide y zero")
else:
    print("result:",result)
finally:
    print("Execution complete")
    
    
            