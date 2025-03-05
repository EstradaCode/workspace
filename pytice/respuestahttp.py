from urllib import request
response = request.urlopen("https://www.youtube.com/")
# con una solicitud! wtffff es solo una función. en java es todo un metodo!!!
print(response)
print(response.getcode())
#print(response.read())