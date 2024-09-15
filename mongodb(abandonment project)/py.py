import pymongo
import dns # required for connecting with SRV
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@<clusterName>.mongodb.net/?retryWrites=true&w=majority")
db = client.<databaseName>