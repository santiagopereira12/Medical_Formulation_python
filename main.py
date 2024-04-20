from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

tabla = [
    {'Paciente': 'Santiago', 'Medico': 'Valeria', 'id_formula': '5', 'cedula_doctor': '13590', 'cedula_paciente': '31795', 'Medicamento': 'Alegrisol', 'Cantidad': '15', 'Observacion': 'Primer Dato', 'Fecha': '2024-04-15'},
    {'Paciente': 'Josefino', 'Medico': 'Nicole', 'id_formula': '6', 'cedula_doctor': '26847', 'cedula_paciente': '24860', 'Medicamento': 'Felicital', 'Cantidad': '15', 'Observacion': 'Segundo Dato', 'Fecha': '2024-04-15'}
]


@app.route('/datos', methods=['GET'])
def obtenerDatos():
    return jsonify(tabla)

@app.route('/paciente/<nombre>', methods=['GET'])
def obtenerPaciente(nombre):
    resultado = [
        dato for dato in tabla if dato['Paciente'] == nombre
    ]
    return jsonify(resultado)

@app.route('/doctor/<nombre>', methods=['GET'])
def obtenerDoctor(nombre):
    resultado = [
        dato for dato in tabla if dato['Medico'] == nombre
    ]
    return jsonify(resultado)

@app.route('/datos', methods=['POST'])
def agregarDato():
    newData = request.json
    tabla.append(newData)
    return jsonify(newData), 201

@app.route('/datos/<int:id_formula>', methods=['PUT'])
def actualizarDato(id_formula):
    updateData = request.json
    for dato in tabla:
        if dato['id_formula'] == str(id):
            dato['Paciente'] = updateData.get('Paciente', dato['Paciente'])
            dato['Medico'] = updateData.get('Medico', dato['Medico'])
            dato['cedula_doctor'] = updateData.get('cedula_doctor', dato['cedula_doctor'])
            dato['cedula_paciente'] = updateData.get('cedula_paciente', dato['cedula_paciente'])
            dato['Medicamento'] = updateData.get('Medicamento', dato['Medicamento'])
            dato['Cantidad'] = updateData.get('Cantiadad', dato['Cantidad'])
            dato['Observacion'] = updateData.get('Observacion', dato['Observacion'])
            dato['Fecha'] = updateData.get('Fecha', dato['Observacion'])
            return jsonify(dato)
    return jsonify({'error': 'No existe el dato'}), 404

@app.route('/datos/<int:id_formula>', methods=['DELETE'])
def eliminarDato(id_formula):
    global tabla
    tabla = [dato for dato in tabla if dato['id_formula'] != id_formula]
    return jsonify({'message': 'Dato eliminado correctamente'}), 200

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
