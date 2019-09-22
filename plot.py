from classes.atmosphere import AtmosphereModel

output_path = "output/earth.csv"

ap = AtmosphereModel("Earth")

output_file = open(output_path, 'w')

output_file.write("alt; T; H; rho; P; mu")

alt_max = 1000000
alt_step = 1000
nstep = int(alt_max / alt_step)

for i in range(nstep):
    alt = i * alt_step
    T = ap.get_T(alt)
    H = ap.get_H(alt)
    rho = ap.get_rho(alt)
    P = ap.get_P(alt)
    mu = ap.get_mu(alt)
    output_file.write("\n{0}; {1}; {2}; {3}; {4}; {5}".format(alt, T, H, rho, P, mu))
