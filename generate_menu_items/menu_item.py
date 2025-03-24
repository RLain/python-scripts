import pandas as pd
import random

# Helper function to generate a unique External ID
def generate_external_id(index):
    prefix = random.choice(['R'])
    return f"{prefix}{str(index).zfill(4)}"

# Helper function to generate a random recipe name
def generate_unique_recipe_name():
    base_names = ['Wrap', 'Noodles', 'Sandwich', 'Salad', 'Bowl']
    modifiers = ['Spicy', 'BBQ', 'Quinoa', 'Mexican', 'Healthy', 'Zesty', 'Asian', 'Light']
    filling = ['Vegetable', 'Fish', 'Beef', 'Chicken', 'Falafel', 'Pork', 'Chicken', 'Beef', 'Cheese', 'Tofu', 'Jackfruit']


    while True:
        base = random.choice(base_names)
        modifier = random.choice(modifiers)
        filling = random.choice(filling)
        name = f"{modifier} {filling} {base}"

        return name

# Generate a random integer between 1 and 1000 for energy and portion weight
def generate_integer_in_range(min_value, max_value):
    return random.randint(min_value, max_value)

# Generate random values for boolean or small categorical fields
def generate_random_binary():
    return random.choice([0, 1])

def generate_random_trinary():
    return random.choice([0, 1, 2])

# Main function to create test data
def generate_test_data(num_rows=100):
    data = []
    
    for i in range(1, num_rows+1):
        row = {
            'External ID': generate_external_id(i),
            'Kitchen ID': 12345,  # Fixed value
            'Name': generate_unique_recipe_name(),
            'Status': random.choice(['active', 'discontinued']),
            'Energy (KCal per 100g)': generate_integer_in_range(1, 1000),
            'Portion Weight (g)': generate_integer_in_range(1, 1000),
            'Ingredients': random.choice(['celery, onion, garlic', 'potato, carrot, peas', 'spinach, tomato, basil']),
            'Halal': generate_random_binary(),
            'Vegan': generate_random_binary(),
            'Vegetarian': generate_random_binary(),
            'Celery': generate_random_trinary(),
            'Egg': generate_random_trinary(),
            'Fish': generate_random_trinary(),
            'Gluten': generate_random_trinary(),
            'Lupine': generate_random_trinary(),
            'Milk': generate_random_trinary(),
            'Mollusc': generate_random_trinary(),
            'Mustard': generate_random_trinary(),
            'Nut': generate_random_trinary(),
            'Peanut': generate_random_trinary(),
            'Sesame': generate_random_trinary(),
            'Shellfish': generate_random_trinary(),
            'Soy': generate_random_trinary(),
            'Sulfites': generate_random_trinary()
        }
        data.append(row)

    # Convert list of dictionaries into a DataFrame
    df = pd.DataFrame(data)

    # Write to Excel file
    output_file = 'test_data.xlsx'
    df.to_excel(output_file, index=False)

    print(f"Test data has been written to {output_file}")

# Call the function to generate data
generate_test_data(110)
