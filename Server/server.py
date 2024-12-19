from flask import Flask, request
import json
#db is within config which is used for the database
from config import db

app = Flask(__name__)

@app.get("/")
def home():
        return "Hello from flask"

@app.get("/test")
def text():
        return "Hello from the test page"

@app.get("/about")
def about():
        return "Jose Torres"

# create an endpoint that says hello using a variable instead of using a string

@app.get("/hello")
def hello():
        message = {"message":"Hey!"}
        return json.dumps(message)


@app.get("/api/products")
def get_products():
        #this was moved from line 26 to here during the database portion
        products = []
        cursor=db.products.find({})
        for prod in cursor:
            products.append(fix_id(prod))
        return json.dumps(products) 

#this was done in the database portion in Mongo
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

@app.post("/api/products")
def save_product():
        product = request.get_json()
        print(f"this is my new product{product}")
        #products.append(product)
        db.products.insert_one(product)
        # (fix_id(product)) was added during the database portion
        return json.dumps(fix_id(product))


@app.put("/api/products/<int:index>")
def update_product(index):
    updated_product = request.get_json()
    print(f"Product: {updated_product}: {index}")

    if 0 <= index <= len(products):
        products[index] = updated_product
        return json.dumps(updated_product)
    else:
        return "That index does not exist"


@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete: {index}")

    if index >= 0 and index < len(products):
        delete_product = products.pop(index)
        return json.dumps(delete_product)
    else:
        return "That index does not exist"

app.run(debug=True) #that when i save the code, the changes are applied to the server