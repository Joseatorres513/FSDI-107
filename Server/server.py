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

@app.get("/api/catalog")
def get_catalog():
    #this if for the catalog portion of the database
    catalog = []
    cursor=db.catalog.find({})
    for cata in cursor:
        catalog.append(fix_id(cata))
    return json.dumps(catalog)


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

@app.post("/api/catalog")
def save_catalog():
        catalog = request.get_json()
        print(f"this is my new catalog{catalog}")
        #catlaog.append(catalog)
        db.catalog.insert_one(catalog)
        # (fix_id(catalog)) was added during the database portion
        return json.dumps(fix_id(catalog))


@app.get("/api/reports/total")
def total_catalog():
    total = []
    cursor=db.catalog.find({})
    for item in cursor:
        total.append(fix_id(item))
    return json.dumps(len(total))

@app.get("/api/products/<category>")
def get_products_by_category(category):
    products = []
    cursor = db.products.find({"category": category})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

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

from bson.objectid import ObjectId

@app.put("/api/products/<id>")
def update_product(id):
    updated_product = request.get_json()
    # Convert string id to ObjectId
    db.products.update_one({"_id": ObjectId(id)}, {"$set": updated_product})
    return json.dumps({"status": "updated", "product": updated_product})