import requests
import json


def get_millennium_falcon_info():
    url = "https://swapi.dev/api/starships/10/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        falcon_info = {
            "название": data["name"],
            "максимальная скорость": data["max_atmosphering_speed"],
            "класс": data["starship_class"],
            "пилоты": []
        }

        # Добавляем информацию о каждом пилоте
        for pilot_url in data["pilots"]:
            pilot_response = requests.get(pilot_url)
            if pilot_response.status_code == 200:
                pilot_data = pilot_response.json()
                homeworld_response = requests.get(pilot_data["homeworld"])
                homeworld_data = homeworld_response.json() if homeworld_response.status_code == 200 else None

                pilot_info = {
                    "имя": pilot_data["name"],
                    "рост": pilot_data["height"],
                    "вес": pilot_data["mass"],
                    "родная планета": homeworld_data["name"] if homeworld_data else None,
                    "ссылка на информацию о родной планете": homeworld_data["url"] if homeworld_data else None
                }

                falcon_info["пилоты"].append(pilot_info)

        return falcon_info
    else:
        # Если запрос неудачен, вывести сообщение об ошибке
        print(f"Ошибка при запросе к API. Код: {response.status_code}")
        return None

# Получаем информацию и выводим в консоль
millennium_falcon_info = get_millennium_falcon_info()
if millennium_falcon_info:
    print(json.dumps(millennium_falcon_info, indent=2))

    # Сохраняем в JSON-файл
    with open("millennium_falcon_info.json", "w") as file:
        json.dump(millennium_falcon_info, file, indent=2)
