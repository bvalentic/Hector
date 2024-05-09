import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('Spotify_2000.csv')
data.rename(columns=lambda x: x.strip(), inplace=True)

# print(data.head())

song_mood = (
    data[['Title', 'Artist', 'Valence', 'Energy', 'Danceability']]
    .assign(Mood_Score=lambda x: x[['Valence', 'Energy', 'Danceability']].mean(axis=1))
    [['Title', 'Artist', 'Mood_Score']]
)
print(song_mood.head())


