# helper.py este es porque quería ver estadísticas de los usuarios generales, como su success rate al tirar para saber que hipótesis o que era más facil de predecir 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Lcarga los csv
df_player = pd.read_csv('data/player_data.csv')
df_shots = pd.read_csv('data/cleaned_data.csv')

# reviso que sean int los id's
df_player['Jug'] = df_player['Jug'].astype(int)
df_shots['Jug'] = df_shots['Jug'].astype(int)

# inner join en el id de los jugadores
df = pd.merge(df_player, df_shots, on='Jug', how='inner')

# calculando el numero de tiros que hizo cada jugador
shots_taken = df.groupby('Jug').size()
success_rate = df.groupby('Jug')['Tiro Default'].mean() # sacando el success rate de cada jugador 

# agregados al data frame para imprimir
df['shots_taken'] = df['Jug'].map(shots_taken)
df['player_success_rate'] = df['Jug'].map(success_rate)

# se agrupa por jugador
player_stats = df.groupby('Jug')[['Tiro Default', 'Tiro 3']].mean()

# acomodados por mejor tiro de fault
print("\nAverage Success Rate per Player in \'Tiro Default\':")
print(player_stats.sort_values(by='Tiro Default', ascending=False))

# acomodados por mejor tiro de tres puntos
print("\nAverage Success Rate per Player in \'Tiro 3\':")
print(player_stats.sort_values(by='Tiro 3', ascending=False))
