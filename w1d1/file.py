int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

def add(a, b):
    x = a + b
    return x

heroes = ["Iron Man", "Hulk", "Wonder Woman", "Thor"]
villains = ["Thanos", "Joker", "Ultron", ["Marvel", "DC"]]

add_vals = add(2, 5)
print(add_vals)


def say_hi(arr):
    for n in arr:
        if type(n) == str:
            print(f"Hi {n}")

say_hi(heroes)
say_hi(villains)

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1
print("Happy New Year, Man!")


for i in range (5, 11):
    print(i)


# for i in range (5, 0, -2):
#     print(i)

ironman = {
    "name": "Tony Stark",
    "bday": "5/29/1970", 
    "weight": 160,
    "powers":{
        "power1" : "Genius",
        "power2" : "Master Engineer"
    }
}

for i in ironman: 
    print(i, ironman[i])

for i in ironman["powers"]: 
    print(i, ironman["powers"][i])

print(ironman["name"])
print(ironman["weight"])
ironman["age"] = 51
print(ironman["powers"]["power2"])


for i in range(0, len(heroes)):
    print(i, heroes[i])

for v in villains:
    print(v)

for md in villains[3]:
    print(md)

#can loop through strings!! villains[0]

from random import randint

print(randint(1,6))

likes_bbq = True
likes_fruit = True
age = "21"
weight = "140"
iq = "122"

print(len(age))

