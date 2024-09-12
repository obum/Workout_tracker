import requests


GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 190
AGE = 32

APP_ID = '2ebbf521'
API_KEY = 'bb0ae86df1e17989a7fcc63da00ba1c2'

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

user_input = input(f'Tell me which exercise you did :')

headers =  {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
    }

parameter = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
    }


response = requests.post(url=url, json=parameter, headers=headers)
# response.raise_for_status()
print(response)

data = response.json()

print(data)
