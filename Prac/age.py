try:
    age=int(input("enter age:"))

    if age<0 or age>120:
        raise ValueError("Invalid age")
    
    print("Valid age:",age)

except ValueError as e:
    print("Error:",e)