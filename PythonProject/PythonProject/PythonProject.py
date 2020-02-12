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
x = np.array(temp)
plt.plot(x, x, label='temp')
plt.legend()
plt.show()



