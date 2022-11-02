name = input("What's your name?")
print("Hey", name, "let's figure out what generation you belong to!")
year = int(input("What year were you born in?"))
if year <= 1925 or year <= 1946:
    print(name, "! You're a Tradionalist!")
elif year <= 1947 or year <= 1964:
    print(name, "! You're a Baby Boomer!")
elif year <= 1965 or year <= 1981:
    print(name, "! You're a Generation Xer!")
elif year <= 1982 or year <= 1995:
    print(name, "! You're a Millenial!")
elif year <= 1996 or year <= 2015:
    print(name, "! You're a Generation Zer!")
else:
    print("I'm sorry", name, ". I have no idea what generation you belong to!")
