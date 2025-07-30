#Create 'sales' data set having 5 columns namely ID, TV , Radio , Newspaper and Sales (random 500 entries ) Build a linear regression model by indentifying independent and target variables split the variable 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 1. Create dataset with ID and noise
np.random.seed(42)
data = pd.DataFrame({
    'ID': np.arange(1, 501),
    'TV': np.random.uniform(10, 300, 500),
    'Radio': np.random.uniform(5, 50, 500),
    'Newspaper': np.random.uniform(0, 100, 500)
})
data['Sales'] = 0.045 * data['TV'] + 0.187 * data['Radio'] + 0.005 * data['Newspaper'] + np.random.normal(0, 1, 500)

# 2. Define independent and target variables
x = data[['TV', 'Radio', 'Newspaper']]  # independent variables
y = data['Sales']                       # target variable

# 3. Split into training and testing sets (70% train, 30% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)

# 4. Print training and testing data
print("Training features (x_train):\n", x_train.head(), "\n")
print("Training target (y_train):\n", y_train.head(), "\n")
print("Testing features (x_test):\n", x_test.head(), "\n")
print("Testing target (y_test):\n", y_test.head(), "\n")

# 5. Build and train the linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# 6. Print model coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("Feature Names:", x.columns.tolist())

# 7. Make predictions
y_pred = model.predict(x_test)

# 8. Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")

# 9. Visualization: Actual vs Predicted Sales
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='teal')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linewidth=2)
plt.title('Actual vs Predicted Sales')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

