#region import area

import numpy as np
import matplotlib.pyplot as plt
#endregion

x = np.linspace(0, 10, 101)
print(x)

y = 4 +2 * np.sin(2*x)
fig, ax = plt.subplots()
ax.plot(x,y,linewidth=2.0)

ax.set(xlim=(0,8), xticks=np.arange(1,8),
       ylim=(0,8), yticks=np.arange(1,8))

plt.show()

