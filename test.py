from classes import planet, vehicle

earth = planet.Planet()




shape = 'ball'
size = (2,) # m
launchspeed = 35000 # m/s
launchaltitude = 100 # m
weight = 10000 # kg
rocket = vehicle.Vehicle(planet = earth, size = size, mass = weight, V = launchspeed, alt = launchaltitude, shape = shape)

F_drag = rocket.get_drag(alt = 10000, V = -500)

print(F_drag)
