from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import routeAuth, routeUser

app = FastAPI()

#CORS

origins = ['https://user-api-cad.herokuapp.com/','http://localhost:3000']

app.add_middleware(CORSMiddleware, allow_origins = origins,
                                   allow_credentials=True, 
                                   allow_methods  = ["*"],
                                   allow_headers =["*"],)

#Routes Users - aut and auth

app.include_router(routeAuth.router, prefix="/auth")

app.include_router(routeUser.router)
