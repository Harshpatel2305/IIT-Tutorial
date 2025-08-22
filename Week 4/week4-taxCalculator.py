income = int(input("enter input:"))

if income <= 20000:
    setTax = income * 0.02
    print(setTax)
else:
    if income <= 50000:
        setTax = 400 + 0.025 * (income - 20000)
        print(setTax)
    else:
        setTax = 1150 + 0.035 * (income - 50000)
        print(setTax)

