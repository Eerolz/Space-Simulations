from classes import planet, vehicle

earth = planet.Planet()
size = (5, 1) # m
launchspeed = 50000 # m/s
launchaltitude = 100 # m
weight = 5000 # kg
rocket = vehicle.Vehicle(planet = earth, size=size, mass = weight, V = launchspeed, alt = launchaltitude)

tstep = 0.0001
time = 25

nsteps = int(time / tstep)

a_max = 0

for i in range(nsteps):
    a, F = rocket.timestep(tstep)
    if abs(a) > a_max:
        a_max = abs(a)
    if rocket.alt < 0 or rocket.V < 0:
        print('\ntime: ' + str(i*tstep))
        break

print('\na max: ' + str(a_max))
print('alt: ' + str(rocket.alt))
print('V: ' + str(rocket.V))
