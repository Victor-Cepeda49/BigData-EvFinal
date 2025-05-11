# **Evidencia Final de 'Infraestructura para Big Data'**

Durante las clases, se creó un conjunto de datos que posteriormente se mejoró y ajustó individualmente en casa. El propósito de este proyecto fue predecir la probabilidad de que un jugador de baloncesto atine a canasta desde diferentes distancias (tiro libre y tiro de 3 puntos). Para ello, se recolectaron datos relevantes de los jugadores y sus habilidades en el tiro.

## **Obtención de los Datos:**
Se recolectaron datos de un equipo de baloncesto, donde se registró el número de aciertos y fallos en tiros libres y tiros de 3 puntos. Los datos se combinaron con información adicional de los jugadores, como su edad, años de experiencia y características físicas (altura y peso). La variable de interés para el modelo fue la tasa de éxito del jugador en los tiros realizados, calculada como el porcentaje de aciertos en relación con el total de intentos.

## **Preprocesamiento de los Datos:**
Para mejorar la calidad de los datos y generar variables más relevantes, se calcularon métricas como la tasa de éxito en los tiros de los jugadores (porcentaje de aciertos en los 10 primeros intentos), lo cual sirvió como una de las características para entrenar los modelos. Además, se realizaron los siguientes pasos:
- **Limpieza de datos:** Se sustituyeron los valores nulos o incorrectos en atributos como edad y años de experiencia con el promedio de esos valores en el conjunto de datos.
- **Generación de nuevas características:** Se creó una nueva variable denominada "shots_taken", que representaba el número de intentos de tiro de cada jugador.
- **Normalización de los datos:** Se normalizaron las variables numéricas para que todos los atributos tuvieran la misma escala, utilizando el **StandardScaler**.

## **Modelos Entrenados:**
Para predecir la tasa de éxito de los jugadores, se entrenaron tres modelos de regresión:
1. **Regresión Lineal**: Un modelo básico de regresión que intenta predecir la tasa de éxito en función de las características de los jugadores.
2. **Random Forest Regressor**: Un modelo más complejo basado en la combinación de múltiples árboles de decisión, que permite capturar relaciones no lineales entre las variables.
3. **Gradient Boosting Regressor**: Un modelo avanzado que combina varios modelos débiles (árboles de decisión) en un conjunto de modelos más fuerte, optimizando el rendimiento mediante el entrenamiento iterativo.

## **Evaluación de los Modelos:**
Cada uno de los modelos fue evaluado utilizando el **Mean Squared Error (MSE)** y el **R² Score**, que son métricas clave para evaluar la precisión de los modelos de regresión.

- **Modelo de Regresión Lineal**:
  - **MSE**: 0.2491
  - **R² Score**: -0.0038

- **Modelo Random Forest Regressor**:
  - **MSE**: 0.2498
  - **R² Score**: -0.0066

- **Modelo Gradient Boosting Regressor**:
  - **MSE**: 0.2491
  - **R² Score**: -0.0038

## **Resultados y Conclusión:**
Aunque los tres modelos no alcanzaron una alta precisión (los valores de R² negativos indican que los modelos no explicaron adecuadamente la variabilidad de los datos), se puede concluir que el enfoque de ingeniería de datos y la selección de variables fueron adecuados. La tasa de éxito en los tiros, combinada con otras características de los jugadores, ofreció una base sólida para los modelos, aunque la calidad de los datos y la falta de otros factores relevantes podrían haber limitado el rendimiento.

## **Lecciones Aprendidas:**
- **Calidad de los Datos:** La calidad de los datos fue un factor clave en el rendimiento del modelo. La mejora de la calidad de los datos (por ejemplo, recolectando más información sobre los jugadores o utilizando datos de tiro en diferentes condiciones) podría mejorar los resultados.
- **Proceso Iterativo:** El proceso de probar diferentes modelos y técnicas de ingeniería de características es fundamental para encontrar la mejor solución para el problema.

Este proyecto no solo demuestra la aplicación de técnicas de regresión en un contexto deportivo, sino que también subraya la importancia de la calidad y el preprocesamiento de los datos en la creación de modelos predictivos.
