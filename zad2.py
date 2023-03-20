import random

cities = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
trip = []
iterations = len(cities)
for x in range(0, iterations):
    ran = random.randint(0, iterations-1)
    trip.append(cities[ran])
    cities.remove(cities[ran])
    iterations -= 1
print(trip)
