import math
"""
THIS IS OLD CODE AND SHOULDN'T BE USED AS IT IS, WE NEED TO DO THINGS PROPERLY
"""



# changing variables:
atmosphere = True
# if true:
fairing_sep = 110 #km
timestep = 0.1 #sec

target_V = 8 #km/s
launch_alt = 0.5 #km
max_G = 5

# constants:
G_0 = 9.78033 #m/s^2
R_0 = 3963 #m
H = 8400 #m
P_0 = 1.225 #kg/m^3
C_drag = 0.9 #drag coefficient PLACEHOLDER
A = 1 #m^2 PLACEHOLDER

def get_P(alt):
    alt = alt*1000 #km to m
    P = P_0 * math.e**(-alt/H)
    return P

def get_G(alt):
    # G_0/G = ((R_0+alt)/R_0)^2
    R2 = ((R_0+alt)/R_0)**2
    # G_0/G = R2 => G = G = G_0/R2
    G = G_0/R2
    return G


def get_Q(alt, V):
    V = V*1000 #km/s to m/s
    P = get_P(alt)
    Q = (P*(V**2))/2
    return Q #Pa

def get_drag(alt, V):
    V = V*1000 #km/s to m/s
    P = get_P(alt)

    F = (1/2)*P*(V**2)*A*C_drag

    return F

print(get_P(5))
