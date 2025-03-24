import itertools
import pandas as pd
import random

def generate_bowl_combinations():
    bowls = ["Mexican bowl", "Poke bowl", "Garden bowl", "Middle eastern bowl", "Field bowl", "Kaleida bowl"]
    proteins = ["Chicken breast", "Falafel", "Beef rump", "Prawns", "Trout", "Tofu"]
    dressings = ["Crushed green herbs", "Soy tapioca dressing", "Sesame labne", "Chamomile dressing"]

    # Generate all possible combinations
    combinations = list(itertools.product(bowls, proteins, dressings))

    # Add a random quantity from 1 to 40
    data = [(bowl, protein, dressing, random.randint(1, 40)) for bowl, protein, dressing in combinations]

    # Convert to DataFrame
    df = pd.DataFrame(data, columns=["Bowl", "Protein", "Dressing", "Quantity"])

    # Write to an Excel file
    df.to_excel("bowl_combinations.xlsx", index=False)
    print("Excel file 'bowl_combinations.xlsx' has been created successfully.")

if __name__ == "__main__":
    generate_bowl_combinations()
