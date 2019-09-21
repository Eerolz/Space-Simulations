from scipy import constants as con
import math
from . import atmosphere

class Planet:
    """Planet class for space simulations"""
    def __init__(self, mass = 5972000000000000000000000, radius = 6371000):
        self.mass = mass
        self.radius = radius
        self.atmosphere = atmosphere.AtmosphereModel(planet = "Earth") #later numbers from elsewhere

        def get_g(self, alt):
            g = (con.G*self.mass)/(self.radius+alt)**2
            return g

        def get_F_gravity(self, mass, distance):
            F = con.G*((self.mass*mass)/distance**2)
            return F
