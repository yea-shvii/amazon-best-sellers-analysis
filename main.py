import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df=pd.read_csv('bestsellers.csv')

#Understanding Data
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

#Cleaning data
df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title","Year": "Publication Year","User Rating": "Rating"},inplace="True")

df["Price"]=df["Price"].astype(float)

#Analyzing Data
author_counts=df['Author'].value_counts()
print(author_counts)

avg_rating_by_genre=df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

#Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

#Export average rating by genre toa CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")


