from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Créer une session Spark
spark = SparkSession.builder.appName("TwitchDataProcessing").getOrCreate()

spark = SparkSession.builder \
    .appName("Connect to HDFS") \
    .master("local[2]") \
    .config("spark.sql.shuffle.partitions", 2) \
    .getOrCreate()

# Connect to HDFS
spark.conf.set("fs.defaultFS", "hdfs://ec2-51-20-83-218.eu-north-1.compute.amazonaws.com:8020")

# List the contents of the root directory
df = spark.sql("SELECT * FROM hdfs.`/`")

# Lire le fichier CSV dans un DataFrame Spark
df = spark.read.option("header", "true").csv("Twitch_game_data.csv")

# Afficher le schéma du DataFrame
df.printSchema()

# Afficher les premières lignes du DataFrame
df.show()

# Calculer la moyenne des heures regardées
avg_hours_watched = df.select("Hours_watched").rdd.map(lambda x: float(x[0])).mean()
print(f"Moyenne des heures regardées : {avg_hours_watched} heures")

# Trouver le mois avec le pic maximum de téléspectateurs
max_peak_viewers_month = df.orderBy(col("Peak_viewers").desc()).select("Month", "Peak_viewers").first()
print(f"Mois avec le pic maximum de téléspectateurs : {max_peak_viewers_month['Month']} avec {max_peak_viewers_month['Peak_viewers']} téléspectateurs")

# Fermer la session Spark
spark.stop()
