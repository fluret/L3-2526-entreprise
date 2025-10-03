age = int(input("Quel est votre âge ? "))

if 8 <= age < 10:
    groupe = "U8"
elif 10 <= age < 12:
    groupe = "U10"
elif 12 <= age < 14:
    groupe = "U12"
elif 14 <= age < 16:
    groupe = "U14"

print("Vous appartenez au groupe :", groupe)