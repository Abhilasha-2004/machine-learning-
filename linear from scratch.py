import numpy as np
import matplotlib.pyplot as plt
#using np.random.seed to generate a numbers dataset randomly 
np.random.seed(0)
X = np.random.rand(1000)
y = 2 * X + 1 + 0.1 * np.random.rand(1000)  

# Calculate the mean of X and y
mean_x = np.mean(X)
mean_y = np.mean(y)
# Calculate the slope (weight)
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
slope = numerator / denominator
# Calculate the intercept (bias)
intercept = mean_y - slope * mean_x
regression_line = slope * X + intercept
#plotting of data based on the above calculated intercept slope and regression line 
plt.scatter(X, y, label='Data Points', color='blue')
plt.plot(X, regression_line, label='Regression Line', color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
#printing calculated slope , intercept and new predicted value 
print("Slope (Weight):", slope)
print("Intercept (Bias):", intercept)
new_x = 0.5  
predicted_y = slope * new_x + intercept
print("Predicted y for new_x:", predicted_y)
