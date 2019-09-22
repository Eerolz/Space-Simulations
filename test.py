from classes import planet, vehicle

earth = planet.Planet()
size = (5, 1) # m
launchspeed = 15000 # m/s
launchaltitude = 100 # m
weight = 5000 # kg
rocket = vehicle.Vehicle(planet = earth, size=size, mass = weight, V = launchspeed, alt = launchaltitude)

for i in range(100):
    alt = rocket.timestep(0.01)
    print(alt)
    if alt < 0:
        break

print(rocket.V)
