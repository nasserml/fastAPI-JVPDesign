from enum import Enum

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def base_get_route():
    return {"message":"hello world"}

@app.post("/")
async def post():
    return {"message" : "hello from the post route"}


@app.put("/")
async def put():
    return {"message" : "hello from the put method"}

@app.get("/users")
async def list_users():
    return {"message" :"List users route"}



@app.get("/users/me")
async def get_current_user():
    return {"message" : "this is the cucrrent user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id" : user_id}


class FoodEnum(str, Enum):
    fruits ="fruits"
    vegetables = "vegetables"
    dairy = "dairy"

# Path Parameters
@app.get("/food/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name,
                "message":"you are healthy"}
    if food_name.value == "fruits":
        return {
            "food_name": food_name,
            "message" : "You are still healthy but like sweet things"
        }
    return {
        "food_name": food_name,
        "message": "I like chocolate Milk"
    }

# Query Parameters
fake_item_db = [
    { "item_name" : "Foo"},
    { "item_name" : "Bar"},
    { "item_name" : "Baz"},
]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_item_db[skip: skip + limit]
# Optional Query and required query parameters
@app.get("/items/{item_id}")
async def get_item(item_id: str,
                   sample_query_param: str,
                   q: str|None = None,
                   short: bool = False):
    item = {"item_id": item_id,
            "sample_query_param": sample_query_param}
    if q:
        item.update({"q":q})
    if not short:
        item.update({
            "description": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
        })
    return item

# Multiple pathes and Queries Parameters
@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: str,
                        q:str | None = None, short: bool= False):

    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({
            "description": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
        })
    return item

