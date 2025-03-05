#manejador de paquetes de python
import json
import requests # se utiliza para solicitudes http más seguido que la libreria nativa
# utilizo py -m pip 
r= requests.get("https://official-joke-api.appspot.com/random_joke")
jsonData= json.loads(r.text)
print(jsonData)
#pyttsx3