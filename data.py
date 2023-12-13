import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("Twitch_game_data.csv")

# Afficher les premières lignes du DataFrame
print(df.head())

# Convertir la colonne 'Hours_watched' en millions d'heures
df['Hours_watched'] = df['Hours_watched'] / 1e8

# Regrouper les données par année et sommer les heures regardées
df_by_year = df.groupby('Year')['Hours_watched'].sum().reset_index()

# Afficher les premières lignes du nouveau DataFrame
print(df_by_year.head())

# Tracer un graphique des heures regardées par année
plt.figure(figsize=(10, 6))
plt.bar(df_by_year['Year'], df_by_year['Hours_watched'], color='skyblue')
plt.title('Total des heures regardées par année')
plt.xlabel('Année')
plt.ylabel('Heures regardées (en millions)')
plt.show()
