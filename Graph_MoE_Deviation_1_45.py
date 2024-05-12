import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


x = np.arange(1, 46)
mean_margins_Data_MoE_desvios_1_45 = [1.0, 0.9700000000000001, 0.8299999999999998, 0.7075, 0.615, 0.601, 0.569, 0.48549999999999993, 0.391, 0.48100000000000004, 0.4, 0.309, 0.36100000000000004, 0.36550000000000005, 0.32249999999999995, 0.30100000000000005, 0.318, 0.3369999999999999, 0.2495, 0.2905, 0.16349999999999998, 0.2325, 0.229, 0.20249999999999999, 0.0905, 0.18100000000000002, 0.173, 0.14400000000000002, 0.1655, 0.15550000000000003, 0.089, 0.09799999999999999, 0.121, 0.1065, 0.1135, 0.1, 0.1125, 0.07900000000000003, 0.0485, 0.097, 0.094, 0.0875, 0.11150000000000002, 0.10200000000000001, 0.06899999999999999]

fit = np.polyfit(np.log(x),mean_margins_Data_MoE_desvios_1_45, 1)
print(fit)
y_predicted = []
for i in range(1, 46):
    y_predicted.append(fit[1] + np.log(i) * fit[0])

plt.plot(x, mean_margins_Data_MoE_desvios_1_45, marker='o', linestyle='-', color='b')
plt.plot(x, y_predicted, color='c')
plt.xlabel('Sample size')
plt.ylabel('Mean Margins of Error')
plt.title('Mean Margins of Error for y_i,N simulated through n(p + deviation)')
plt.grid(True)
plt.show()