from fastapi import status

## Prueba para crear un cliente
def test_create_customer(client_test):
    response = client_test.post( 
        "/customers/", 
        json={
            "name": "John",
            "email": "john@example.com", 
            "age": 30, 
            "description": "John Doe Test"
        },
    )
    
    assert response.status_code == status.HTTP_201_CREATED



## Prueba para leer un cliente
def test_read_customer(client_test):
    response = client_test.post( # Siempre post
        "/customers/", 
        json={ # Datos del cliente a crear
            "name": "John",
            "email": "john@example.com", 
            "age": 30, 
            "description": "John Doe Test"
        },
    )
    
    customer_id: int = response.json()["id"] # Obtener el ID del cliente creado
    response_read = client_test.get(f"/customers/{customer_id}") # Leer el cliente creado

    """
    Verificar que el cliente creado sea el mismo que el leído
    """

    assert response_read.json()["name"] == "John"
    assert response_read.json()["email"] == "john@example.com"
    assert response_read.json()["age"] == 30
    assert response_read.json()["description"] == "John Doe Test"
    assert response_read.status_code == status.HTTP_200_OK
    