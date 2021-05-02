with open('Currency data.txt') as f:
    lines=f.readlines()
    currencyDict={}
    for line in lines:
        parsed=line.split('\t')
        currencyDict[parsed[0]]=parsed[1]

amount=int(input("Enter the amount you want to convert to:"))
print("Enter the currency you want to convert your Amount to\n")
[print(item) for item in currencyDict.keys()]
currency=input("Enter one of the values:")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")