import uvicorn
from fastapi import FastAPI, Body, Depends

from app.model import AdvisorSchema, UserSchema, UserLoginSchema
from app.auth.auth_bearer import JWTBearer
from app.auth.auth_handler import signJWT


advisors = [
    {
        "id": 1,
        "name": "Advisor 1 ",
        "info": "Rest of information for advisor."
    },
    {
        "id": 2,
        "name": "Advisor 2 ",
        "info": "Rest of information for advisor."
    },
    {
        "id": 3,
        "name": "Advisor 3",
        "info": "Rest of information for advisor."
    },
]

users = []

app = FastAPI()

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


# route handlers

# testing
@app.get("/", tags=["root"])
def greet():
    return {"ping": "pong!."}


# Get Advisors
@app.get("/advisors", tags=["Advisors Methods"])
def get_advisors():
    return { "data": advisors }


@app.get("/advisors/{id}", tags=["Advisors Methods"])
def get_single_advisor(id: int):
    if id > len(advisors):
        return {
            "error": "No such advisor with the supplied ID."
        }

    for advisor in advisors:
        if advisor["id"] == id:
            return {
                "data": advisor
            }


@app.post("/advisors", dependencies=[Depends(JWTBearer())], tags=["Advisor Protected Methods "])
def add_advisor(advisor: AdvisorSchema):
    advisor.id = len(advisors) + 1
    advisors.append(advisor.dict())
    return {
        "data": "advisor added."
    }


@app.post("/user/signup", tags=["users"])
def create_user(user: UserSchema = Body(...)):
    users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.email)


@app.post("/user/login", tags=["users"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Bad credentials!"
    }
