## Put and Delete- HTTP verbs
## working with API's -- Json 

from flask import Flask, jsonify, request
app = Flask(__name__)

# Initial data in my to do list 
items = [
    {"id": 1, "name": "Buy milk",'Description':'item 1'},
    {"id": 2, "name": "Walk the dog",'Description':'item 2'},
    {"id": 3, "name": "Do laundry",'Description':'item 3'}
]

@app.route('/')
def home():
    return "Welcome 2Do list"

## GET method to get all items in the list

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## Get: retreive a specific item by id

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"Error":'Item not found'})
    return jsonify(item)

## Post: Create a new task
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error":'Invalid data'})
    new_item = {
        "id": items[-1]["id"]+1 if items else 1,
        "name": request.json['name'],
        "Description":request.json['Description']
    }
    items.append(new_item)
    return jsonify(new_item)

# Put: Update an existing item

@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id']==item_id),None)
    if item is None:
        return jsonify({"Error":'Item not found'})
    item['name'] = request.json.get('name',item['name'])
    item['Description'] = request.json.get('Description',item['Description'])
    return jsonify(item)


#DELETE : Delete an item 
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result':"item deleted"})

if __name__ == "__main__":
    app.run(debug = True)

