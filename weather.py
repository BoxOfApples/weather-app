import requests
A = "48534e6daec4966aae103210c01f918f"
c = input("Введмте город: ")
u = f"http://api.openweathermap.org/data/2.5/weather?q={c}&appid={A}&units=metric"
r = requests.get(u)
if r.status_code == 200:
    d = r.json()
    t = d["main"]["temp"]
    w = d["weather"][0]["description"]
    print(f"Температура в {c}:{t}")
    print(f"Погода {w}")
else:
    print("ошибка")