from fastapi import FastAPI
from .views import views

app = FastAPI()
app.include_router(views.router)
