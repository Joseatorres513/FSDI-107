import pymongo
import certifi

# this is the connection string that I got from the mongo db connection and i replaced the password with my actual password
con_string = "mongodb+srv://joseatorres513:Tocachu1$@cluster0.nsc8y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_string, tlsCAFile = certifi.where())
db = client.get_database("ch53_2")