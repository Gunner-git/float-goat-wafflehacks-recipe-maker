import csv
import sqlite3

"""
Input ingredients from User
"""

availableIngredientList = []
ingredientInput = open("api/ingredient_list.txt", "r")
strIngredientInput = ingredientInput.read()

availableIngredientList = strIngredientInput.split('\n')

"""
Input ingredients from db
"""
connection = sqlite3.connect('db/db.db')

c = connection.cursor()

for i in range(1,3):
    neededIngredientList = []

    c.execute(
        f"""
        SELECT * FROM 'Recipe-Ingredients' WHERE("Recipe ID"={i})
        """
    )
    queryOutput = c.fetchall()
    for row in queryOutput:
        ingredient = row[2]
        altIngredient = row[3]
        neededIngredientList.append(ingredient)
        neededIngredientList.append(altIngredient)
    print(neededIngredientList)

print(availableIngredientList)

connection.commit()
connection.close()