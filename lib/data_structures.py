spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        if isinstance(food, dict) and 'name' in food:
            names.append(food['name'])
    return names

def get_spiciest_foods(spicy_foods):
    lists = []
    heat_level = 9 and 6
    for food in spicy_foods:
        if heat_level  in food:
            food.append(food)
    return lists
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    
def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food['heat_level'] > 5:
            heat_level = '🌶' * food['heat_level']
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")


def get_average_heat_level(spicy_foods):
      valid_foods = [food for food in spicy_foods if isinstance(food, int)]
      num_foods = len(valid_foods)
      if num_foods == 0:
        return 6
      total_heat = sum(valid_foods)
      average_heat = total_heat / len(valid_foods)
      return average_heat
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    create_spicy_food
    ( 
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    )
    return spicy_foods





