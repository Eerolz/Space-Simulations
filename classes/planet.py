from scipy import constants as con
import math

class Planet:
    """Planet class for space simulations"""
    def __init__(mass, radius):
        self.mass = mass
        self.radius = radius
        self.atmosphere = Atmosphere()

        def get_g(altitude):
            g = (con.G*self.mass)/(self.radius+altitude)**2
            return g

        def get_F_gravity(mass, distance):
            con.G*(()/altitude)


        def get_air(altitude):
            return self.atmosphere.get_air(altitude)



class Atmosphere:
    """Atmosphere for Planet class."""
    def __init__(P_0, H):
        self.P_0 = P_0 #kg/m^3 // density at sea level
        self.H = H #m, scale height

    def get_P(altitude):
        """Density (kg/m^3) at altitude (m)"""
        P = self.P_0 * math.e**(-altitude/self.H)
        return P

    def get_Re():
        return False # TODO: calculate Reynolds number

    def get_air(altitude):
        P = self.get_P(altitude)
        Re = self.get_Re()
        return {'P':P, 'Re':Re}
