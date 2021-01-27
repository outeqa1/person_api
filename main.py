from flask import Flask, request, jsonify
from person import Person, iin_is_valid

app = Flask(__name__)

people = []


@app.route('/api/v1/people/', methods=['GET', 'POST'])
def people_route():
    if request.method == 'GET':
        if len(people) == 0:
            return {'error': 'data not found'}, 200
        response = []
        for person in people:
            response.append(person.get_json())
        return jsonify(response), 200

    if request.method == 'POST':
        request_json = request.get_json()
        iin = request_json['iin']

        if iin_is_valid(iin):
            new_person = Person(iin)
            people.append(new_person)
            return new_person.get_json(), 201

        return {'error': 'Not valid request.'}, 400


@app.route('/api/v1//people/<iin>/', methods=['GET'])
def get_person(iin):
    for person in people:
        if iin == person.iin:
            return person.get_json(), 200
    return {'error': 'data not found'}, 404


app.run(debug=True)
