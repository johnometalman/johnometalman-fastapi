
from fastapi import FastAPI, Request
from db import  create_all_tables
from .routers import customers, transactions, invoices, extras, plans
import time


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













