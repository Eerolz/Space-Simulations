import math
from scipy import constants as con

class AtmosphereModel():
    """Atmosphere model for the planet class."""
    def __init__(self, planet = None, g_0 = None, T_0 = None, rho_0 = None, molM = None):
        if planet is not None:
            g_list = {'Venus': 8.87, 'Earth': 9.807, 'Mars': 3.71, 'Titan': 1.352}
            T_list = {'Venus': 737, 'Earth': 288, 'Mars': 210, 'Titan': 94}
            rho_list = {'Venus': 65, 'Earth': 1.217, 'Mars': 0.02, 'Titan': 19.85}
            molM_list = {'Venus': 0.04345, 'Earth': 0.02897, 'Mars': 0.04334, 'Titan': 0.0274}
            self.g_0 = g_list[planet]    # Surface gravity
            self.T_0 = T_list[planet]    # Surface temperature
            self.rho_0 = rho_list[planet]    # Surface density
            self.molM = molM_list[planet]    # Molecular weight of air
        else:
            self.g_0 = g_0
            self.T_0 = T_0
            self.rho_0 = rho_0
            self.molM = molM

    def get_H(self, alt):
        T = self.T_0 * math.e**(-alt/200)    # Temperature model based on Earth atmosphere
        H = con.R * T / (self.molM * self.g_0)    # Scale height (m)

        return H

    def get_rho(self, alt):
        H = self.get_H(alt)
        rho = self.rho_0 * math.e**(-altm/H)    # Density (kg/m^3)

        return rho

    def get_Q(self, alt, V):
        rho = self.get_rho(alt)
        Q = (rho*(V**2))/2    # Pressure (Pa)

        return Q
