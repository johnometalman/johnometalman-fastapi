
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from db import  create_all_tables
from .routers import customers, transactions, invoices, extras, plans
import time
from typing import Annotated


app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(extras.router)
app.include_router(plans.router)


# Este es un middleware para ver los logs de las peticiones, debo importar Request
@app.middleware("http") # Debo pasarle el http
async def log_request_time(request: Request, call_next):
    start_time = time.time() # Da un punto de partida
    response = await call_next(request) # Ejecuta la petición
    process_time = time.time() - start_time # Calcula el tiempo de procesamiento
    print(f"Request {request.url} processed in {process_time:.4f} seconds") # Imprime el tiempo de procesamiento
    return response




# Importando security, credentials y status implementamos en Root un acceso controlado que se imprime en consola simulando un usuaurio
security = HTTPBasic()

@app.get("/")
async def root(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    print(credentials)
    if credentials.username == "johnometalman" and credentials.password == "123456test":
        return {"message": f"Hola {credentials.username}"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")


# Basicamente, defino security como una instancia de HTTPBasic() y luego la uso como dependencia en la función root, luego 
# dependiendo de las credenciales que se envien, se ejecutara la función root que valida si es correcto o no el acceso










