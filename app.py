from flask import Flask, request, jsonify
import random
import string
import os

app = Flask(__name__)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    try:
        # Récupérer les données envoyées par le client
        data = request.get_data(as_text=True)

        # Sauvegarder les données dans un fichier (par exemple, 'OutServer.txt')
        with open('OutServer.txt', 'w') as file:
            file.write(data)

        # Retourner une réponse de succès
        return jsonify({'message': 'Data received successfully!'}), 200

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

@app.route('/receive-data', methods=['GET'])
def get_data():
    try:
        # Lire les données du fichier
        if os.path.exists('OutServer.txt'):
            with open('OutServer.txt', 'r') as file:
                data = file.read()
        else:
            data = "print('')"

        return data, 200

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
