from pprint import pprint

university = "fiu "

print(university)
print(type(university))
print(university[0])
print(university[1])
print(university[2])
print(university[3])

print(university.title())
print(university.upper())
print(university.lower())

first_name = "greg"
last_name = "reis"
print(first_name, last_name)
print("fiu","miami",1965,54000,True)
print(first_name + last_name)
print(first_name + " " + last_name)

print(f"Professor {first_name.title()} {last_name.title()} teaches courses at FIU.")

a = 10
b = 3

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division
print(a // b) # floor division
print(a ** b) # a to the power of b (exponentiation)
print(a % b) # modulo (the remainder of the division of a by b)

singers = ["mariah","beyonce","lana","billie","rihanna"]

print(type(singers))
print(singers[0])
print(singers[1])
print(singers[-1])
singers.append("taylor")
print(singers)
singers.extend(["miley","sade","kelly"])
print(singers)
singers.remove("lana")
print(singers)
singers.insert(2,"leona")
print(singers)
singers[1] = "anitta"
print(singers)
print(len(singers))
print(singers.count("mariah"))
print(singers.index("rihanna"))

x = singers.pop(6)
print(x)
print(singers)

print(singers[3:5]) # accessing positions 3 and 4
print(singers[5:]) # accessing positions 5 and onward
print(singers[:6]) # accessing from beginning all the way to position 5
print(singers[:]) # a copy of the original list

singers.sort()
print(singers)
singers.sort(reverse=True)
print(singers)

for i in singers:
    print(i.title())
print("FIU")

water_data = {
    "temperature": [78,86,92],
    "salinity": [55,67,68],
    "oxygen" : [7.2, 6.7, 3.5]
}

print(water_data)
print(type(water_data))
print(water_data["oxygen"])

print(water_data.keys())
print(water_data.values())

for j,k in water_data.items():
    print(f"Parameter {j} values are: {k}.")

water_data["pH"]=[7.2, 7.3, 7.4]

from pprint import pprint

pprint(water_data)

import pandas as pd # structured data manipulation package

df = pd.DataFrame(water_data)
print(df)

print(df.describe())
print(df.info())
print(df["pH"])
print(df["temperature"].min())

df.to_csv("water_data.csv")