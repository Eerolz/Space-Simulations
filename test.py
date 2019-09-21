from classes import planet, vehicle

earth = planet.Planet()
size = (5, 1) # m
launchspeed = 15000 # m/s
weight = 500 # kg
rocket = vehicle.Vehicle(planet = earth, size=size, weight = weight, V = launchspeed)
print(rocket.get_drag())
