from classes import planet, vehicle

earth = planet.Planet()
size = (5, 1) # m
launchspeed = 15000 # m/s
launchaltitude = 100 # m
weight = 5000 # kg
rocket = vehicle.Vehicle(planet = earth, size=size, mass = weight, V = launchspeed, alt = launchaltitude)

tstep = 0.0001
time = 10

nsteps = int(time / tstep)

for i in range(nsteps):
    alt = rocket.timestep(tstep)
    print(alt)
    if alt < 0:
        break

print('\n' + str(rocket.V))