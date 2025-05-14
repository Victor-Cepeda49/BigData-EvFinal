#Prueba con un agente externo usando Gradient Boosting Regressor

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import StandardScaler
from data_loader import load_and_prepare_data

# Datos del agente externo 
shots_taken = 5
player_success_rate = 0.43  # 0.6

# Crear arreglo con los datos
new_data = np.array([[shots_taken, player_success_rate]])

# Cargar los datos para entrenar el modelo 
X_train, X_test, y_train, y_test = load_and_prepare_data()

# Crear y entrenar el modelo Gradient Boosting
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
model.fit(X_train, y_train)

# Escalar los datos del agente externo
scaler = StandardScaler()
scaler.fit(X_train)
new_data_scaled = scaler.transform(new_data)

# Hacer la predicción
prediction = model.predict(new_data_scaled)

# Mostrar resultado
print(f"Predicción (probabilidad de encestar) con Gradient Boosting: {prediction[0]:.2f}")

