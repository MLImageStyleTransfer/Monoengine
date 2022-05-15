import uvicorn
from fastapi import FastAPI

from app.utils import get_port
from app.views import views

app = FastAPI()
app.include_router(views.router)


if __name__ == '__main__':
    uvicorn.run("runner:app", host='0.0.0.0', port=get_port("BACKEND"), reload=True, debug=True)
