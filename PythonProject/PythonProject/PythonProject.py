date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
temp = [25, 21, 16, 18, 15, 20, 18, 15, 17, 19]
import numpy as np
np_date = np.array(date)
np_temp = np.array(temp)
mean = (np.mean(np.array(temp)))
min = (np.amin(np.array(temp),0))
max = (np.amax(np.array(temp),0))
dict = {"date": [np_date],
        "temp": [np_temp],
        "mean temp": [mean],
        "min temp": [min],
        "max temp": [max]}
import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
#x = np.array(temp)

# Plot the data
#plt.plot(x, x, label='temp')

# Add a legend
#plt.legend()

# Show the plot
#plt.show()



import matplotlib.pyplot as plt

# Initialize the plot
fig = plt.figure()
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)

# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(x,y)

# Show the plot
plt.show()

