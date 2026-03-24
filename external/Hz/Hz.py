from classy import Class
import numpy as np
from matplotlib import pyplot as plt

cosmo = Class()
cosmo.compute()
z_arr = np.logspace(0, 4, 1000) - 1
Hz_arr = [cosmo.Hubble(z) for z in z_arr]

for z, Hz in zip(z_arr, Hz_arr):
    print("%.18g %.18g" % (z, Hz))

# np.savetxt("external/Hz/Hz_table.dat", np.column_stack((z_arr, Hz_arr)), fmt="%.18g", header="z    H(z) [1/Mpc]", comments='# ')


# plt.plot(z_arr, Hz)
# plt.xlabel('Redshift z')
# plt.ylabel('Hubble parameter H(z) [1/Mpc]')
# plt.title('Hubble Parameter as a Function of Redshift')
# plt.grid()
# plt.show()