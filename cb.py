import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("Twitch_game_data.csv")

# Convertir la colonne 'Hours_watched' en millions d'heures
df['Hours_watched'] = df['Hours_watched'] / 1e6

# Filtrer le DataFrame pour le jeu "Cyberpunk 2077"
cyberpunk_df = df[df['Game'] == 'Cyberpunk 2077']

# Regrouper les données par année et sommer les téléspectateurs moyens
cyberpunk_by_year = cyberpunk_df.groupby('Year')['Avg_viewers'].sum().reset_index()

# Afficher les premières lignes du nouveau DataFrame
print(cyberpunk_by_year.head())

# Tracer un graphique des téléspectateurs moyens pour "Cyberpunk 2077" par année
plt.figure(figsize=(10, 6))
plt.bar(cyberpunk_by_year['Year'], cyberpunk_by_year['Avg_viewers'], color='orange')
plt.title('Nombre de vues pour "Cyberpunk 2077" par année')
plt.xlabel('Année')
plt.ylabel('Nombre moyen de téléspectateurs')
plt.show()
