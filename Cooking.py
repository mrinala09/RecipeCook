import requests

def fetch_recipe(ingredient):
    # Replace 'YOUR_APP_ID' and 'YOUR_APP_KEY' with your actual Edamam API credentials
    app_id = '25d85249'
    app_key = '5c1b4b2708f131ccffa8c79cabe63657'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'

    response = requests.get(url)
    if response.status_code == 200:
        ### Status code 200 means its true, the response is the recipe pmuch and it contains the ingredients and stuff.
        return response.json()
        #reponse is the recipe being returned
    else:
        print(f"Failed to fetch recipe. Status code: {response.status_code}")
        return None

def display_recipe(recipe):
    if not recipe or 'hits' not in recipe:
        ###If the key is not found in the recipe then the recipe is an L and hence shall not be chosen.
        print("No recipe found.")
        return

    for idx, hit in enumerate(recipe['hits'], 1):
        ###Enumerate basically prints the index AND the value, which in this case is the recipe. The hits thingymabob is the KEY that is searched for in the recipe in the API. The little 1 at the end just starts the index value at one. 
        item = hit['recipe']
        #Item is going to be the recipe printed, hit and hits is different, but basically do the same thing except reverse, the recipe is passed into the key to basically check if its present to determine whether that recipe will be printed.
        print(f"{idx}. {item['label']}")
        #The label or name of the recipe
        print("   Ingredients:")
        for ingredient in item['ingredientLines']:
            print(f"   - {ingredient}")
            ###this just prints the ingredients, each one on a diff line
        print("   Instructions:")
        print(f"   {item['url']}\n")
        ###A link that shows instructions on how to make the recipe

def main():
    name = input("What is your name?: ")
    print(f"Hello, {name }")
    ingredient = input("Enter an ingredient (if you want multiple, type them with commas, ex: chicken, sauce,...): ")
    recipes = fetch_recipe(ingredient)
    display_recipe(recipes)

if __name__ == "__main__":
    main();
