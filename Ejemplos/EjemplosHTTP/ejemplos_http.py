import requests as req


#  GET
def getRequest():
    urlGet = "https://jsonplaceholder.typicode.com/posts/1"
    getResponse = req.get(urlGet)

    if getResponse.status_code == 200:
        data = getResponse.json()
        print("Respuesta del servidor:")
        print(data)
    else:
        print("Error al realizar la solicitud.")


# POST
def postRequest():
    urlPost = "https://jsonplaceholder.typicode.com/posts"
    postData = {"title": "Mi título", "body": "Contenido del post", "userId": 1}

    postResponse = req.post(urlPost, json=postData)
    print(postResponse.content)
    if postResponse.status_code == 201:
        print("Datos enviados correctamente.")
    else:
        print("Error al enviar los datos.")


# PUT
def putRequest():
    urlPut = "https://jsonplaceholder.typicode.com/posts/1"
    putData = {
        "title": "Título actualizado",
        "body": "Contenido actualizado",
        "userId": 1,
    }

    putResponse = req.put(urlPut, json=putData)

    if putResponse.status_code == 200:
        print("Recurso actualizado correctamente.")
    else:
        print("Error al actualizar el recurso.")


if __name__ == "__main__":
    # getRequest()
    # postRequest()
    putRequest()
