import pandas as pd
import numpy as np



movie_data = pd.read_csv("../input/imdb.csv")



movie_grouped = movie_data.groupby(['movie']).agg({'ratingCount': 'count'}).reset_index()
group_sum = movie_grouped['ratingCount'].sum()
movie_grouped['percentage'] = movie_grouped['ratingCount'].div(group_sum)*100
movie_grouped.sort_values(['ratingCount', 'movie'], ascending = [0, 1])

train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)


