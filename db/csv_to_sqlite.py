import sqlite3
import pandas as pd

df = pd.read_csv('db/CulinaryDB/04_Recipe-Ingredients_Aliases.csv')
df1 = pd.read_csv('db/CulinaryDB/01_Recipe_Details.csv')
df3 = pd.read_csv('db/CulinaryDB/03_Compound_Ingredients.csv')
df2 = pd.read_csv('db/CulinaryDB/02_Ingredients.csv')


df.columns = df.columns.str.strip()
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()
df3.columns = df3.columns.str.strip()

connection = sqlite3.connect('db.db')

df.to_sql('Recipe-Ingredients', connection, if_exists="replace")

connection.close()

connection = sqlite3.connect('db.db')

df1.to_sql('Recipe-Details', connection, if_exists="replace")

connection.close()

connection = sqlite3.connect('db.db')

df2.to_sql('Ingredients', connection, if_exists="replace")

connection.close()

connection = sqlite3.connect('db.db')


df3.to_sql('Compound-Ingredients', connection, if_exists="replace")

connection.close()