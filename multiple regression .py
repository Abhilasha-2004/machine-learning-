import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])  
y = np.array([100, 200, 300])  


model = LinearRegression()


model.fit(X, y)


new_data = np.array([[2, 3, 4], [5, 6, 7]])  
predictions = model.predict(new_data)


print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

print("Predictions:", predictions)
