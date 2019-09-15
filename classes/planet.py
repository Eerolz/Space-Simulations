from scipy import constants as con
import math
import atmosphere

class Planet:
    """Planet class for space simulations"""
    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius
        self.atmosphere = AtmosphereModel(planet = "Earth") #later numbers from elsewhere

        def get_g(self, alt):
            g = (con.G*self.mass)/(self.radius+alt)**2
            return g

        def get_F_gravity(self, mass, distance):
            F = con.G*((self.mass*mass)/distance**2)
            return F

        def get_air(self, alt):
            rho = self.atmosphere.get_rho(alt)
            air = {'rho':rho}
            return air
