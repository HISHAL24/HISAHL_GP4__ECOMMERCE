from flask import Flask, request, jsonify
from flask_cors import CORS
from dto.catalogue_dto import catalogue
from service.catalogue_service import catalogueService

app = Flask(__name__)
CORS(app)

service = catalogueService()

@app.route("/catalogues", methods=["GET"])
def get_all_catalogues():
    return jsonify(service.get_all_catalogues())

@app.route("/catalogues/<int:catalogue_id>", methods=["GET"])
def get_catalogue_by_id(catalogue_id):
    result = service.get_catalogue_by_id(catalogue_id)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Catalogue not found"}), 404

@app.route("/catalogues", methods=["POST"])
def create_catalogue():
    data = request.get_json()
    c = catalogue(**data)
    service.create_catalogue(c)
    return jsonify({"message": "Catalogue created"}), 201

@app.route("/catalogues/<int:catalogue_id>", methods=["PUT"])
def update_catalogue(catalogue_id):
    data = request.get_json()
    c = catalogue(**data)
    service.update_catalogue_by_id(catalogue_id, c)
    return jsonify({"message": "Catalogue updated"})

@app.route("/catalogues/<int:catalogue_id>", methods=["DELETE"])
def delete_catalogue(catalogue_id):
    service.delete_catalogue_by_id(catalogue_id)
    return jsonify({"message": "Catalogue deleted"})

if __name__ == "__main__":
    app.run(debug=True)

