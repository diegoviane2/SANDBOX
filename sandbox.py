# Import json module
import json

# Define json variable of nested data
nestedData = """{
 "watch":{
  "men":{
   "brand":"Titan",
    "price":200
  },
  "women":{
   "brand":"Citizen",
   "price":250
  },
  "kid":{
   "brand":"Blancpain",
   "price":100
  }
 }
}"""

# Load the json data
watchlist = json.loads(nestedData)

# Search 'brand' for women
if 'brand' in watchlist['watch']['kid']:
 print(watchlist['watch']['kid']['brand'])