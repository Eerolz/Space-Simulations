from scipy import constants as con

class Vehicle:
    def __init__(self, size, mass, planet = None, shape = 'cylinder', alt = 0, V = 0, propulsion = None, fuel = 0, fuel_usage = None):
        # dimension arguments vary with shape
        if len(size) != 2 and shape == 'cylinder':
            raise Exception('Shape "{}" takes 2 parameters for size. (lenght, diameter)')
        elif len(size) != 1 and shape == 'ball':
            raise Exception('Shape "ball" takes 1 parameter for size. (diameter)')
        self.size = size
        self.shape = shape # shape of the Vehicle
        self.mass = mass # dry mass (kg)
        self.planet = planet # the planet Vehicle is on
        self.propulsion = propulsion # N
        self.fuel = fuel # kg
        self.fuel_usage = fuel_usage # kg/s
        self.alt = alt # altitude (m)
        self.V = V # speed (m/s), currently verticality assumed

    def get_drag(self, alt = None, V = None):
        if not alt:
            alt = self.alt
        if not V:
            V = self.V
        if not self.planet or V == 0 or alt >= 100000:
            return 0

        if self.shape == 'cylinder':
            l = self.size[0] # lenght
            d = self.size[1] # diameter
            A_cross = con.pi * (d / 2)**2    # assuming circular cross-section
            A_wet = (con.pi * d * l) + A_cross    # assuming cylinder-like shape
        elif self.shape == 'ball':
            r = self.size[0] / 2
            l = con.pi * r # half of the circumference
            A_cross = con.pi * r**2
            A_wet = 4 * con.pi * r**2
        else:
            raise Exception('Shape "{}" is not yet implemented for drag.'.format(self.shape))

        Be = self.planet.atmosphere.get_Be(alt, V, l)
        Re = self.planet.atmosphere.get_Re(alt, V, l)
        C_d = (A_wet / A_cross) * (Be / Re**2)    # Drag coefficient

        rho = self.planet.atmosphere.get_rho(alt)
        drag = 0.5 * rho * C_d * A_cross * V**2    # Drag force (N)

        return drag

    def propel(self, time):
        fuel_time = self.fuel/self.fuel_usage # s
        if fuel_time > time:
            self.fuel -= self.fuel_usage * time
            return self.propulsion
        elif 0 < fuel_time < time:
            self.fuel = 0
            return self.propulsion * (fuel_time/time)
        elif fuel_time == 0:
            self.propulsion = 0
            return self.propulsion

    def timestep(self, ts = 1, propulsion_direction = 0):
        """Do a timestep:
        ts is the lenght of the timestep
        propulsion direction: 0=no propulsion, -1=accelerate down, 1=accelerate up"""

        F_drag = self.get_drag()
        F_g = self.planet.get_F_gravity(self.mass, alt = self.alt)
        if propulsion_direction:
            F_propulsion = self.propel(ts)*propulsion_direction
        else:
            F_propulsion = 0
        if self.V >= 0:
            F_total = F_propulsion - F_drag - F_g
        else:
            F_total = F_propulsion + F_drag - F_g
        a = F_total / (self.fuel + self.mass) # acceleration (m/s^2)
        self.V += a * ts
        self.alt += self.V * ts

        return a, F_total
