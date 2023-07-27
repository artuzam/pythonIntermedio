import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

#  GET
getResponse = requests.get(url)

if getResponse.status_code == 200:
    data = getResponse.json()
    print("Respuesta del servidor:")
    print(data)
else:
    print("Error al realizar la solicitud.")

# POST
postData = {"title": "Mi título", "body": "Contenido del post", "userId": 1}

postResponse = requests.post(url, json=postData)

if postResponse.status_code == 201:
    print("Datos enviados correctamente.")
else:
    print("Error al enviar los datos.")

# PUT
putData = {"title": "Título actualizado", "body": "Contenido actualizado", "userId": 1}

putResponse = requests.put(url, json=putData)

if putResponse.status_code == 200:
    print("Recurso actualizado correctamente.")
else:
    print("Error al actualizar el recurso.")
