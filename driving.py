country = input("where are you come from? ")
age = input("what is your age? ")
age = int(age)
if country == "Taiwan":
	if age >= 18:
		print("You have driving licence qualify")
	else:
		print("You do't have driving licence qualify  ")
elif country == "American":
	if age >= 16:
		print("You have driving licence qualify")
	else:
		print("You do't have driving licence qualify  ")