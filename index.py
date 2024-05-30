import requests,json
key = "62966bfeff7f30551ce0f44578c9e240"
city = input("Enter the city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
res = requests.get(url)
if res.status_code == 200:
    print("success")
    result = res.json()
    city_name = result['name']
    weather = result['weather'][0]['main']
    temp = result['main']['temp']
    feel = result['main']['feels_like']
    info = [city_name,weather,temp,feel]
    for i in info:
        print(i)
else:
    print("error fetching the city!!")
    
    
