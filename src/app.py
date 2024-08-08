import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import matplotlib.pyplot as plt

# load the .env file variables
load_dotenv()

#3) Variables entorno:

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

#4) Iniciar la biblioteca de Spotify:

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="client_id",
    client_secret="client_secret",
    redirect_uri="http://localhost/",
))

#5) Realizar solicitudes a la API:

client_credential_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) 

sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)

fito = '1tZ99AnqyjgrmPwLfGU5eo'
response = sp.artist_top_tracks(fito)
#print(response)

#6) Transformar Pandas en DataFrame

response = sp.artist_top_tracks('1tZ99AnqyjgrmPwLfGU5eo')
if response:
  # We keep the "tracks" object of the answer
  df = pd.DataFrame(columns = ['namber', 'popularity', 'time'])
  tracks = response["tracks"]
  for track in tracks:
    name = track['name']
    popu = track['popularity'] 
    time = int(track['duration_ms'])/(1000*60)
    df=pd.concat([df,pd.DataFrame({'name':name,'popularity':popu,'time':time}, index = [0])], ignore_index = True)
#print(df)

# 6.1) Ordeno las canciones por popularidad creciente:
df_popularity = df.sort_values('popularity')
#print(df_popularity)

#6.2) Muestro el top 3
#df_popularity.head()
#df_popularity.nlargest(3, popu)

#print(df[:3])

#7) Análisis estadístico:

#7.1) Gráfico correlación entre popularidad y duración de la canción:
scatter_plot = sns.scatterplot(data = df, x = 'popularity', y = 'time')
fig =scatter_plot.get_figure()
fig.savefig("scatter_plot.png")

plt.show()

"""
CONCLUSIÓN: 
El gráfico muestra que, a pesar de que se puede observar una ligera tendencia positiva entre la popularidad de una canción y su duración, no existe suficiente evidencia para afirmar que existe correlación entre  ambas variables. 
Es necesario analizar una muestra más amplia para poder evaluar la correlación entre variables.
