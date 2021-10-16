import cmath
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


fig = plt.figure()
ax = plt.axes(projection='3d')

x = 100000
keys = np.linspace( -x, x, 4000)
print( len( keys ) )

values = np.array( [ cmath.sqrt(i) for i in ( np.add( np.multiply( keys, 9 ), 7 ) ) ] )

print( f"Plotting { keys } against { values } ..." )

ax.plot3D( values.imag, values.real, keys )

ax.set_xlabel("i")
ax.set_ylabel("y")
ax.set_zlabel("n")


plt.show()
