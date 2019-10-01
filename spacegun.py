from classes import planet, vehicle

earth = planet.Planet()

shape = 'ball'
size = (2,) # m

# shape = 'cylinder'
# size = (5, 1) # m

launchspeed = 35000 # m/s
launchaltitude = 100 # m
weight = 10000 # kg
rocket = vehicle.Vehicle(planet = earth, size = size, mass = weight, V = launchspeed, alt = launchaltitude, shape = shape)

tstep = 0.0001
time = 600

nsteps = int(time / tstep)

a_max = 0
alt_max = 0

print('ARGUMENTS: ')
print('launchspeed: ' + str(launchspeed))
print('shape: ' + shape)
print('size: ' + str(size))
print('weight: ' + str(weight))

print('\nRESULTS: ')
for i in range(nsteps):
    a, F = rocket.timestep(tstep)
    if abs(a) > a_max:
        a_max = abs(a)
    if rocket.alt > alt_max:
        alt_max = rocket.alt
    # if rocket.alt < 0 or rocket.V < 0 or rocket.alt > 100000:
    if rocket.alt < 0:
        print('time: ' + str(i*tstep))
        break

print('a max: ' + str(a_max))
print('alt:' + str(rocket.alt))
print('alt max: ' + str(alt_max))
print('V: ' + str(rocket.V))
