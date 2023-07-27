import requests as req

url = "https://jsonplaceholder.typicode.com/posts/1"


#  GET
def getRequest():
    getResponse = req.get(url)

    if getResponse.status_code == 200:
        data = getResponse.json()
        print("Respuesta del servidor:")
        print(data)
    else:
        print("Error al realizar la solicitud.")


# POST
def postRequest():
    postData = {"title": "Mi título", "body": "Contenido del post", "userId": 1}

    postResponse = req.post(url, json=postData)
    print(postResponse.content)
    if postResponse.status_code == 201:
        print("Datos enviados correctamente.")
    else:
        print("Error al enviar los datos.")


# PUT
def putRequest():
    putData = {
        "title": "Título actualizado",
        "body": "Contenido actualizado",
        "userId": 1,
    }

    putResponse = req.put(url, json=putData)

    if putResponse.status_code == 200:
        print("Recurso actualizado correctamente.")
    else:
        print("Error al actualizar el recurso.")


if __name__ == "__main__":
    getRequest()
    postRequest()
    putRequest()
