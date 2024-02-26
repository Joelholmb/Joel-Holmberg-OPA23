import numpy as np
import pandas as pd
import plotly.express as px

def load_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        next(file)  # Hoppar över rubrikraden
        for line in file:
            width, height = line.strip().replace('(','').replace(')','').split(',')
            data.append([float(width), float(height)])
    return np.array(data)

def calculate_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def classify_point(test_point, pichu_data, pikachu_data):
    distances = []
    for point in pichu_data:
        distances.append((calculate_distance(test_point, point), 'Pichu'))
    for point in pikachu_data:
        distances.append((calculate_distance(test_point, point), 'Pikachu'))
    distances.sort(key=lambda x: x[0])
    nearest = distances[:5]
    pichu_count = sum(1 for _, label in nearest if label == 'Pichu')
    return 'Pichu' if pichu_count > 2 else 'Pikachu'

# Laddar in data
pichu_array = load_data_from_file('Data/pichu.txt')
pikachu_array = load_data_from_file('Data/pikachu.txt')

# Definiera en testpunkt
test_point = np.array([25, 35])

# Klassificerar testpunkten
classification = classify_point(test_point, pichu_array, pikachu_array)
print(f"Du står närmst en: {classification}")

# Konverterar Numpy arrays till Pandas DataFrame
df_pichu = pd.DataFrame(pichu_array, columns=['Bredd', 'Höjd'])
df_pichu['Art'] = 'Pichu'
df_pikachu = pd.DataFrame(pikachu_array, columns=['Bredd', 'Höjd'])
df_pikachu['Art'] = 'Pikachu'
df_test = pd.DataFrame([test_point], columns=['Bredd', 'Höjd'])
df_test['Art'] = f'Du - {classification}'

df_all = pd.concat([df_pichu, df_pikachu, df_test], ignore_index=True)

# Visualiserar datan med Plotly Express
fig = px.scatter(df_all,
x='Bredd',
y='Höjd',
color='Art',
title='Pichu eller Pikachu?',
labels={'Art': 'Klassificering'}
)
fig.show()


