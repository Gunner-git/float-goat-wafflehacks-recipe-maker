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

for i in range(1,50):
    neededIngredientList = []
    presentIngredientList = []
    toBuyIngredientList = []
    recipeValid = 0

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
    # print(neededIngredientList)

    for item in neededIngredientList:
        if item in availableIngredientList:
            recipeValid = 1
            presentIngredientList.append(item)
        else:
            toBuyIngredientList.append(item)

    if recipeValid == 1:
        c.execute(
            f"""
            SELECT Title FROM 'Recipe-Details' WHERE("Recipe ID"={i})
            """
        )
        recipeTitle = c.fetchone()
        print(f"""
              *********************************************\n\n
              With these ingredients, you can make {recipeTitle}.\n\n
              Ingredients necessary to make that are available are {presentIngredientList}.\n\n
              Ingredients you need to buy are {toBuyIngredientList}.\n\n
              *********************************************\n\n
              """)
    else:
        toBuyIngredientList = []

# print(availableIngredientList)

connection.commit()
connection.close()