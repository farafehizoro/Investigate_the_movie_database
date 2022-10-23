import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

#fuction definition
def replace_zero(serie): 
    serie.replace(0,np.nan, inplace=True)
    return;
    
df_movie=pd.read_csv("tmdb-movies.csv")

#dataset description
df_movie.info()
df_movie.head(2)
df_movie.describe()

#Data cleaning: (documentation)
df_movie.drop(columns=['imdb_id','cast','homepage','director','tagline','keywords','overview','genres','production_companies','release_date'],inplace=True)

#drop duplicated
sum(df_movie.duplicated())
df_movie.drop_duplicates(inplace=True)

#data type conversion
df_movie['budget_adj']=df_movie['budget_adj'].astype(int)
df_movie['revenue_adj']=df_movie['revenue_adj'].astype(int)

replace_zero(df_movie['revenue'])
replace_zero(df_movie['revenue_adj'])
replace_zero(df_movie['budget'])
replace_zero(df_movie['budget_adj'])
replace_zero(df_movie['runtime'])
