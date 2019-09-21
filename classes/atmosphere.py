import math
from scipy import constants as con

class AtmosphereModel():
    """Atmosphere model for the planet class."""
    def __init__(self, planet = None, g_0 = None, T_0 = None, rho_0 = None, P_0 = None, molM = None, mu_0 = None):
        if planet is not None:
            g_list = {'Venus': 8.87, 'Earth': 9.807, 'Mars': 3.71, 'Titan': 1.352}
            T_list = {'Venus': 737, 'Earth': 288, 'Mars': 210, 'Titan': 94}
            rho_list = {'Venus': 65, 'Earth': 1.217, 'Mars': 0.02, 'Titan': 19.85}
            molM_list = {'Venus': 0.04345, 'Earth': 0.02897, 'Mars': 0.04334, 'Titan': 0.0274}
            mu_list = {'Venus': None, 'Earth': 0.00001789, 'Mars': None, 'Titan': None}
            P_list = {'Venus': None, 'Earth': 1.e5, 'Mars': None, 'Titan': None}
            alpha_list = {'Venus': None, 'Earth': 0.000021109, 'Mars': None, 'Titan': None}
            self.g_0 = g_list[planet]    # Surface gravity (m/s^2)
            self.T_0 = T_list[planet]    # Surface temperature (K)
            self.rho_0 = rho_list[planet]    # Surface density (kg/m^3)
            self.P_0 = P_list[planet]    # Surface pressure (Pa)
            self.molM = molM_list[planet]    # Molecular weight of air
            self.mu_0 = mu_list[planet]    # Surface dynamic viscosity (Pa*s)
        else:
            self.g_0 = g_0
            self.T_0 = T_0
            self.rho_0 = rho_0
            self.P_0 = P_0
            self.molM = molM
            self.mu_0 = mu_0

    def get_T(self, alt):
        T = self.T_0 * math.e**(-alt/2.e5)    # Temperature model based on Earth atmosphere

        return T

    def get_H(self, alt):
        T = self.get_T(alt)
        H = con.R * T / (self.molM * self.g_0)    # Scale height (m)

        return H

    def get_rho(self, alt):
        H = self.get_H(alt)
        rho = self.rho_0 * math.e**(-alt/H)    # Density (kg/m^3)

        return rho

    def get_P(self, alt):
        H = self.get_H(alt)
        P = self.P_0 * math.e**(-alt/H)    # Ambient pressure (Pa)

        return P

    def get_Q(self, alt, v):
        rho = self.get_rho(alt)
        Q = (rho * (v**2))/2    # Dynamic pressure (Pa)

        return Q

    def get_mu(self, alt):
        T = self.get_T(alt)
        mu = self.mu_0 * (T / self.T_0)**0.7    # Dynamic viscosity (Pa s)

        return mu

    def get_Re(self, alt, v, l):
        mu = self.get_mu(alt)
        rho = self.get_rho(alt)
        Re = (rho * v * l) / mu    # Reynolds number

        return Re

    def get_Be(self, alt, v, l):
        Q = self.get_Q(alt, v)
        P = self.get_P(alt)
        mu = self.get_mu(alt)
        rho = self.get_rho(alt)

        dP = (Q + P) - P    # Pressure difference across l
        nu = mu / rho    # Momentum diffusivity (m^2/s)
        Be = dP * l**2 / (mu * nu)    # Bejan number

        return Be
