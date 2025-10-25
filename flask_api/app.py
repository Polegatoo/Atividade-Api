from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def get_hello():
    return jsonify({"message": "Hello from Flask API!"})

@app.route("/hello", methods=["POST"])
def create_hello():
    data = request.get_json()
    name = data.get("name", "sem nome")
    return jsonify({"message": f"Hello, {name}!"}), 201

@app.route("/hello", methods=["PUT"])
def update_hello():
    data = request.get_json()
    new_msg = data.get("message", "mensagem padrão")
    return jsonify({"updated_message": new_msg})

@app.route("/hello", methods=["DELETE"])
def delete_hello():
    return jsonify({"message": "Recurso deletado (simulação)"}), 200

if __name__ == "__main__":
    app.run(debug=True)
