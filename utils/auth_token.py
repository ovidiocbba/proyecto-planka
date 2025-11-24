
from utils.config import BASE_URI, USER_EMAIL, USER_PASSWORD
from src.routes.request import PlankaRequests

def generate_token():
    url = f"{BASE_URI}/access-tokens"
    payload = {
            "emailOrUsername": USER_EMAIL,
            "password": USER_PASSWORD
    }
    headers = {'Content-Type': 'application/json'}
    response = PlankaRequests.post(url, headers, payload)
    response_json = response.json()
    #Borrar luego
    print(response_json)
    access_token = response_json['item']
    return access_token


if __name__ == "__main__":
    # print(generate_token())
    token = generate_token()
    if token:
        print("Token generado:", token)
    else:
        print("No se pudo generar el token")
