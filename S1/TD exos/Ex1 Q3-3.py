age = int(input("Quel est votre âge ? "))

message = "Vous appartenez au groupe : "
if age < 8:
    message = "Trop jeune"
elif age < 10:
    message += "U8"
elif age < 12:
    message += "U10"
elif age < 14:
    message += "U12"
elif age < 16:
    message += "U14"
else:
    message = "Trop vieux"

print(message)