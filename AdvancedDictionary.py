#  p1 

geography= {"continets": ["North America", "South America", "Africa", "Antarctica", "Australia", "Asia", "Europe"]}

geography["oceans"] = "Pacific", "Atlantic", "Indian", "Arctic"

print(geography)

# p2

patient= {"name": "John Doe", "age": 25, "height": 64, "symptoms": "cough" }

patient.update({"height": 72})

print(patient)

# p3

print(patient.items())

# p4

print(patient.get("name"))

# p5

print(patient.get("weight", 150))

# p6

print(patient.clear())

# p7

stock_qty= {"cookies": 3200, "bread": 500, "crackers": 52000, "chips": 2000}
new_stock_qty=[]
for key, value in stock_qty.items():
    if(value > 2000):

        new_stock_qty.append(value - 500)

print(new_stock_qty)

# p8

list= [10, 9, 88, 20, 9, 20, 22, 101, 68, 10, 108, 33, 9, 53]

newList = dict({

})

for item in list:
    if(item in newList):
        newList[item] = newList[item] + 1
    else: newList[item] = 1
print(newList)