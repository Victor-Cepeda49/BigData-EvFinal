# data_loader.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_prepare_data():
    # cargo los archivos
    df = pd.read_csv("data/cleaned_data.csv")
    player_df = pd.read_csv("data/player_data.csv")

    # inner join en Jug
    df = df.merge(player_df, on="Jug")

    # normalizando datos 
    df["age"] = df["age"].replace(0, df["age"].mean())
    df["years_exp"] = df["years_exp"].replace(0, df["years_exp"].mean())

    # Feature engineering (romar las caracteristicas que creo que serán mejor por jugador)
    df['shots_taken'] = df.groupby('Jug')['Jug'].transform('size')
    df['player_success_rate'] = df.groupby('Jug')['Tiro Default'].transform('mean')

    # el target o resultado es 0 o 1
    y = df['Tiro Default']

    # Features variables que intentamos utilizar para hacer mejor al algoritmo
    # X = df[['shots_taken', 'player_success_rate', 'height_cm', 'weight_kgs', 'age', 'years_exp', 'plays_sports']]
    X = df[['shots_taken', 'player_success_rate']]

    # entrenando los datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalizar valores numericos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
