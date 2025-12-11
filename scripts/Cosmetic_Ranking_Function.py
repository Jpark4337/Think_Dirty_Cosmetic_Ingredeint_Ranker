import sqlite3

db_path = "/Users/jaypark/Desktop/Computer Science Project/Think Dirty/data/Cosmetic Ingredients.db"  
ingredient_ranks = {
    "Water": 0,
    "CITRIC ACID": 1, #Mild Irritant
    "CHAMOMILE" : 4, #Pregnant Women Use with Caution, may cause uterine contractions
    "Phenoxyethanol":5} #Potential Neurotoxin, may cause vomiting and diarrhea.

# Now I have to make a function!
def update_ingredient_ranks():
    conn = sqlite3.connect(db_path) #this connect the database with the code
    cur = conn.cursor()

    cur.execute("SELECT rowid, Ingredients FROM cosmetics") #This statement excute saying all the products and their ingredients (note: they are separated by commas)
    products = cur.fetchall()  #

    for product_id, ingredients_list_str in products:
        highest_rank = 0 #We start the total score at 0. And then we will track the highest score found.
        max_rank_limit = 8 #Assuming the maxiumum rank for an ingredient is 8. Note (I am not sure if Think Dirty uses this scale or they use weighted average)
        
        if ingredients_list_str:
            ingredients = [item.strip() for item in ingredients_list_str.split(',')] #The ingredients in the row are comma separated!
            
            for ingredient in ingredients:
                if ingredient in ingredient_ranks:
                    score = ingredient_ranks[ingredient]

                    if score > highest_rank:
                        highest_rank = score 

            final_product_rank = min(highest_rank, max_rank_limit) #Therefore, if the highest rank was more than 8, the final product rank will be 8 as the function is min

            cur.execute("""
    UPDATE cosmetics 
    SET Rank = ?
    WHERE rowid = ?
""", (final_product_rank, product_id))

    conn.commit()
    conn.close()
    print(f"Database ranks updated successfully for {len(products)} products.")

if __name__ == "__main__":
    update_ingredient_ranks()