class Property:
	def __init__(self, worth):
		self.worth = worth

	def calculate_tax(self):
		return 0


class Apartment(Property):
	def __init__(self, worth):
		super().__init__(worth)

	def calculate_tax(self):
		return self.worth / 1000


class Car(Property):
	def __init__(self, worth):
		super().__init__(worth)

	def calculate_tax(self):
		return self.worth / 200


class CountryHouse(Property):
	def __init__(self, worth):
		super().__init__(worth)

	def calculate_tax(self):
		return self.worth / 500


money = float(input("Введите количество ваших денег: "))
property_worth = float(input("Введите стоимость вашего имущества: "))

apartment = Apartment(property_worth)
car = Car(property_worth)
country_house = CountryHouse(property_worth)

tax_apartment = apartment.calculate_tax()
tax_car = car.calculate_tax()
tax_country_house = country_house.calculate_tax()

total_tax = tax_apartment + tax_car + tax_country_house

print(f"Налог на квартиру: {tax_apartment}")
print(f"Налог на машину: {tax_car}")
print(f"Налог на дачу: {tax_country_house}")
print(f"Общий налог: {total_tax}")

if money < total_tax:
	print(f"Вам не хватает {total_tax - money} денег")
else:
	print("У вас достаточно денег для уплаты налогов")