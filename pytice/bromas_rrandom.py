import json
import requests
import pyttsx3 as speaker
class Broma:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline
    def __str__(self) -> str:
        return f"{self.setup}\n{self.punchline}"
    def __repr__(self) ->str:
        return self.__str__()


bromas=[]
url="https://official-joke-api.appspot.com/random_ten"
#hay un problema con ssl por la https, se pasó a http
response = requests.get(url)
if(response.status_code==200):
    data= response.text
    jsonData= json.loads(data) # si fuera el random, solo devuelve el string, sino es un diccionario
    # tengo el json ahora necesito serializar los datos
    for j in jsonData:
        setup = j["setup"]
        punchline = j["punchline"]
        bromas.append(Broma(setup,punchline))
    i=0
    speaker.speak("preparate oyente! estas a punto de escuchar 10 chistes verdaderamente buenos en perfecto inglés! comenzamos!!")
    for broma in bromas:
        speaker.speak(broma.setup)
        speaker.speak(broma.punchline)
else:
    print("error en la conexion con la pagina, no se obtuvo respuesta")