# data-cleaner.py
import pandas as pd

# Cargando los datos del excel proporcionado
df = pd.read_excel('data/BD3_DATOSev3.xlsx', skiprows=2) #porque empezamos desde la fila 3

# Pimprimir la estructura original (mas que nada para debugger porque desde linux es dificil abrir archivos xlsx)
print("Original DataFrame:")
print(df.head())

# Se seleccionan las columnas que me importan
df_selected = df[['Ronda','Jug', 'Tiro Default', 'Tiro 3']].copy()

# borrando datos donde el valor es nulo o NaN
df_selected = df_selected.dropna(subset=['Jug', 'Tiro Default'])

# me empezó a salir el error que lo agarraba como float entonces me aseguré que fuera int en el proceso de limpiada de datos
df_selected['Jug'] = df_selected['Jug'].astype(int)

# remplazando si y no por datos booleanos 1 y 0 para los dos tipos de tiro
df_selected['Tiro Default'] = df_selected['Tiro Default'].replace({'si': 1, 'no': 0})
df_selected['Tiro 3'] = df_selected['Tiro 3'].replace({'si': 1, 'no': 0})

# borrar los datos que no eran ni 0 ni 1 (errores de captura de datos)
df_selected = df_selected[df_selected['Tiro Default'].isin([1, 0])]
df_selected = df_selected[df_selected['Tiro 3'].isin([1, 0])]

# imprimir para debugging
print("Cleaned DataFrame:")
print(df_selected)

# guardar a CSV porque es Linux friendly
df_selected.to_csv('data/cleaned_data.csv', index=False)
print("The data has been saved to 'cleaned_data.csv'")
