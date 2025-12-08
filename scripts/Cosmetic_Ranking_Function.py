import sqlite3

db_path = "/Users/jaypark/Desktop/Cosmetic Ingredients.db"  
ingredient_ranks = {
    "Water": 0,
    "CITRIC ACID": 1, #Mild Irritant
    "CHAMOMILE" : 4, #Pregnant Women Use with Caution, may cause uterine contractions
    "Phenoxyethanol":5} #Potential Neurotoxin, may cause vomiting and diarrhea.

# Now I have to make a function!
def update_ingredient_ranks():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT rowid, Ingredients FROM cosmetics")
    products = cur.fetchall()

    for product_id, ingredients_list_str in products:
        total_rank_score = 0.0
        
        if ingredients_list_str:
            ingredients = [item.strip() for item in ingredients_list_str.split(',')] #The ingredients in the row are comma separated!
            
            for ingredient in ingredients:
                if ingredient in ingredient_ranks:
                    total_rank_score += ingredient_ranks[ingredient]

        cur.execute("""
            UPDATE cosmetics 
            SET Rank = ?
            WHERE rowid = ?
        """, (total_rank_score, product_id))

    conn.commit()
    conn.close()
    print(f"Database ranks updated successfully for {len(products)} products.")

if __name__ == "__main__":
    update_ingredient_ranks()