from scipy import constants as con
import math
import atmosphere

class Planet:
    """Planet class for space simulations"""
    def __init__(mass, radius):
        self.mass = mass
        self.radius = radius
        self.atmosphere = Atmosphere(1.225, 8400) #numbers for earth

        def get_g(altitude):
            g = (con.G*self.mass)/(self.radius+altitude)**2
            return g

        def get_F_gravity(mass, distance):
            con.G*(()/altitude)


        def get_air(altitude):
            return self.atmosphere.get_air(altitude)
