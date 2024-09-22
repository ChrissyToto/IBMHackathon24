import requests
from dotenv import load_dotenv
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def getResponse(input_text, restrictions, allergens, budget, goals, cuisines):
    load_dotenv()
    api_key = os.getenv('WATSON_API_KEY')
    authenticator = IAMAuthenticator(api_key)

    token = authenticator.token_manager.get_token()

    url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"
    
    print(input_text)  # Check the input for debugging  

    if len(restrictions) > 1:
        restrictions_str = ", ".join(restrictions[:-1]) + " and " + restrictions[-1]
    else:
        restrictions_str = restrictions[0]  # Only one restriction

    # Form the final sentence
    formatted_string = f". I have the following diet restrictions: {restrictions_str}"

    
    if len(allergens) > 1:
        allergens_str = ", ".join(allergens[:-1]) + " and " + allergens[-1]
    else:
        allergens_str = allergens[0]  # Only one restriction

    # Form the final sentence
    allergens_string = f". I have the following allergens: {allergens_str}"

    budget_string = f". I have the following budget: {budget}"
    if budget == "":
        budget_string = ""

    if len(goals) > 1:
        goals_str = ", ".join(goals[:-1]) + " and " + goals[-1]
    else:
        goals_str = allergens[0]  # Only one restriction

    goals_string = f". I have the following goals: {goals_str}"

    if len(cuisines) > 1:
        cuisines_str = ", ".join(cuisines[:-1]) + " and " + cuisines[-1]
    else:
        cuisines_str = cuisines[0]  # Only one restriction

    cuisines_string =  f". The cuisines I prefer are: {cuisines_str}"


    input_text = input_text + formatted_string + allergens_string + budget_string + goals_string + cuisines_string
    print(input_text)
    body = {	
    "input": """You'\''ll act as a dietitian who'\''s current with the latest data research. Always keep in mind dietary preferences, restrictions and health conditions. Respond only to queries about food, recipes, or nutrition. 
    For any other topics, reply with '\''I cannot assist you with that.'\'' Before finalizing any response, confirm that the query is entirely related to food, recipes, or nutrition and ensure that all dietary restrictions are thoroughly thought of in the response. If any part of it is not, use the fallback response: '\''I cannot assist you with that.'\''. After creating a response, ensure that it is formatted clearly for readability and free of grammatical errors.

    Input: Create a step-by-step recipe for a delicious and healthy breakfast smoothie. Include a list of ingredients, measurements, and detailed instructions:
    Output: **Strawberry & Banana Green Smoothie**

    *Ingredients:*
    - 1 cup fresh spinach
    - 1/2 frozen banana
    - 1/2 frozen strawberries
    - 1/2 cup unsweetened almond milk
    - 1 tablespoon fresh lemon juice
    - 1 tablespoon honey or maple syrup (optional)

    *Instructions:*

    1. Add all ingredients to a high-speed blender.

    2. Blend until smooth, adding more almond milk if needed for desired consistency.

    3. Pour the smoothie into a glass and garnish with a slice of banana, strawberry, or a sprig of fresh mint, if desired.

    4. Enjoy this nutritious and delicious breakfast smoothie!

    This smoothie is packed with vitamins, minerals, and antioxidants from the spinach, banana, and strawberries. The lemon juice adds a burst of tanginess, and the almond milk provides plant-based protein and healthy fats. The optional honey or maple syrup can be added for a touch of natural sweetness.

    Input: Create a meal plan for someone allergic to nuts.
    Output: **Meal Plan for a Nut-Allergic Person**

    **Day 1:**
    - Breakfast: Greek yogurt with berries and honey
    - Lunch: Quinoa salad with chickpeas, tomatoes, cucumber, and red onion
    - Dinner: Stuffed bell peppers with quinoa and black beans

    **Day 2:**
    - Breakfast: Overnight oats with chia seeds, almond milk, and mixed berries
    - Lunch: Avocado toast on whole grain bread with cherry tomatoes and sprouts
    - Dinner: Lentil curry with sweet potatoes and spinach

    **Day 3:**
    - Breakfast: Smoothie with spinach, banana, strawberries, and almond milk
    - Lunch: Egg salad sandwich on whole grain bread with lettuce, tomato, and cucumber
    - Dinner: White bean and vegetable stir-fry with brown rice

    **Day 4:**
    - Breakfast: Chia pudding with coconut milk, sliced banana, and honey
    - Lunch: Whole grain crackers with avocado, cucumber, and cherry tomatoes
    - Dinner: Quinoa and vegetable stir-fry with tamari sauce

    **Day 5:**
    - Breakfast: Yogurt with granola and sliced banana
    - Lunch: Chickpea salad with mixed greens, tomatoes, and red onion
    - Dinner: Spinach and cheese tortellini soup with a side of whole grain bread

    This meal plan provides a variety of nut-free meals that are packed with nutrients and flavor. The Greek yogurt with berries and honey is a delicious and protein-rich breakfast, while the quinoa salad with chickpeas and stuffed bell peppers with quinoa and black beans are hearty and satisfying lunches and dinners. The avocado toast and egg salad sandwich are great options for a lighter meal, and the chickpea salad and spinach and cheese tortellini soup are perfect for when you need something warm and comforting.

    Input: Explain to me the theory of everything
    Output: I cannot assist you with that

    
    Input: Explain to me the theory of everything. I have the following diet restrictions: None. I have the following allergens: None. I have the following budget: £10
    Output: I cannot assist you with that

    Input: Suggest a protein shake recipe. 
    I am allergic to nuts and bananas.
    I have a budget of less that £10.
    I am 80kg.
    Output:  **Basic Protein Shake**

    *Ingredients:*
    - 1 scoop of your favorite protein powder (e.g., whey, plant-based)
    - 1 cup of your favorite milk (e.g., dairy, almond, soy, oat)
    - 1 banana (optional)
    - 1 tablespoon of honey or maple syrup (optional)
    - 1 cup of ice

    *Instructions:*

    1. Add all ingredients to a blender, except for the ice.

    2. Blend until smooth, adding more milk if needed for desired consistency.

    3. Taste and add more sweetener if desired.

    4. Pour the shake into a glass and garnish with a slice of banana or a sprig of fresh mint, if desired.

    This basic protein shake is an affordable and customizable option for anyone looking to increase their protein intake. The protein powder can be adjusted based on your preference, and the milk can be swapped out for a dairy-free alternative if needed. The banana adds natural sweetness and creaminess, but it can be omitted for a vegan or lactose-free version. This shake can be made in large batches and stored in the refrigerator for quick and easy meals throughout the week.

    Input: {}

    Output:""".format(input_text),
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 5000,
            "stop_sequences": [
			    "I cannot assist you with that"
		    ],
            "repetition_penalty": 1
        },
        "model_id": "ibm/granite-13b-chat-v2",
        "project_id": "be17dd82-782f-4b9f-bb78-e2cbc37ac44e",
        "moderations": {
            "hap": {
                "input": {
                    "enabled": True,
                    "threshold": 1,
                    "mask": {
                        "remove_entity_value": True
                    }
                },
                "output": {
                    "enabled": True,
                    "threshold": 1,
                    "mask": {
                        "remove_entity_value": True
                    }
                }
            }
        }
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()
    print(data)
    return data['results'][0]['generated_text']
