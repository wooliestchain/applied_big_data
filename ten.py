import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame Pandas
df = pd.read_csv("Twitch_game_data.csv")

# Convertir la colonne 'Hours_watched' en millions d'heures
df['Hours_watched'] = df['Hours_watched'] / 1e6

# Regrouper les données par jeu et calculer la somme des téléspectateurs moyens
top_games = df.groupby('Game')['Avg_viewers'].sum().reset_index()

# Trier les jeux par la somme des téléspectateurs moyens de manière décroissante
top_games = top_games.sort_values(by='Avg_viewers', ascending=False)

# Sélectionner les dix premiers jeux
top_10_games = top_games.head(10)

# Afficher les premières lignes du DataFrame avec les dix premiers jeux
print(top_10_games)

# Tracer un graphique des dix premiers jeux par somme des téléspectateurs moyens
plt.figure(figsize=(12, 8))
plt.bar(top_10_games['Game'], top_10_games['Avg_viewers'], color='green')
plt.title('Top 10 des jeux par somme des téléspectateurs moyens')
plt.xlabel('Jeux')
plt.ylabel('Somme des téléspectateurs moyens')
plt.xticks(rotation=45, ha='right')  # Rotation des étiquettes pour une meilleure lisibilité
plt.show()
