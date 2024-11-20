from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

user_integer = None

class IntegerInput(BaseModel):
    value: int

@app.get("/")
async def root():
    return {"message": "Hello World"}


# This uses a query parameter. The endpoint can be extended.
@app.get("/enter_integer")
async def enter_integer(value: int):
    global user_integer
    user_integer = value
    return {"message": f"Integer {user_integer} received successfully"}

# This is a path parameter. The endpoint is updated.
@app.get("/enter_integer_required/{value}")
async def enter_integer(value: int):
    global user_integer
    user_integer = value
    return {"message": f"Integer {user_integer} received successfully"}


@app.get("/get_sums")
async def enter_integer(num1: int, num2: int):
    total = num1 + num2
    return {"message": f"Total {total}"}


@app.get("/get_incremented_value")
async def get_incremented_value():
    if user_integer is None:
        raise HTTPException(status_code=400, detail="No integer has been entered yet.")
    return {"incremented_value": user_integer + 1}
