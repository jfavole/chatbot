#########################################################
#
# Data prep script for Kaggle moves data
# Based on https://github.com/Sundar0989/Movie_Bot/blob/master/data/Data_Preparation.ipynb
#
#########################################################

#########################################################
#
# Package and data imports
#
#########################################################

import pandas as pd
import ast

metadata = pd.read_csv('movies_metadata.csv', low_memory=False)

#########################################################
#
# EDA
#
#########################################################

print('Metadata head:')
print(metadata.head())

print('Show null values for each feature:')
print(metadata.isnull().sum())

#########################################################
#
# Modify dataset and write to CSV
#
#########################################################

# Drop NAs and certain columns, add new columns generated from existing data

metadata = metadata.dropna(subset=['imdb_id', 'poster_path'])
metadata = metadata.drop(['belongs_to_collection', 'homepage', 'popularity', 'tagline', 'status', 'runtime', 'release_date', 'original_language', 'production_countries', 'production_companies', 'spoken_languages', 'video'], axis=1)

print('Head modified metadata set:')
print(metadata.head())

metadata['genres'] = metadata['genres'].apply(lambda x: ast.literal_eval(x))
metadata['genres'] = metadata['genres'].apply(lambda x: ', '.join([d['name'] for d in x]))

metadata['imdbURL'] = 'https://www.imdb.com/title/' + metadata['imdb_id'] + '/'
metadata['tmdbURL'] = 'https://www.themoviedb.org/movie/' + metadata['id']
metadata['ImageURL'] = 'https://image.tmdb.org/t/p/w92' + metadata['poster_path']

# Review data
print('Show null values for each feature in updated dataset:')
print(metadata.isnull().sum())

print('Updated metadata set head:')
print(metadata.head())

metadata.to_csv('metadata_prep.csv')
