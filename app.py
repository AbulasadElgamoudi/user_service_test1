# user_service.py

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    '1': {'name': 'Alice', 'email': 'alice@example.com'},
    '2': {'name': 'Bob', 'email': 'bob@example.com'}
}


@app.route('/')
def home():
    return "user Service is Live!"

@app.route('/user/<id>')
def user(id):
    user_info = users.get(id, {})
    return jsonify(user_info)

# Create (Post) a new user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    new_id = str(len(users) + 1)
    users[new_id] = data
    return jsonify({'message': 'user created successfully', 'user_id': new_id}), 201

# Update (Put) an existing user by its ID
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    if id in users:
        data = request.json
        users[id].update(data)
        return jsonify({'message': 'user updated successfully'})
    else:
        return jsonify({'error': 'user not found'}), 404

# Delete (Delete) a user by its ID
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return jsonify({'message': 'user deleted successfully'})
    else:
        return jsonify({'error': 'user not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    