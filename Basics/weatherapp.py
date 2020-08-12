import requests

def weather():
    city=input("Enter your city name :")
    Api_Add='https://api.openweathermap.org/data/2.5/weather?q={}&appid=ff63a0add53fa8dde5d654dc4f08534a'.format(city)
    jsonData=requests.get(Api_Add).json()
    format1=jsonData['weather'][0]['main']
    format2=jsonData['weather'][0]['description']


    print(format1)
    print(format2)

weather()