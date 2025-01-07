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

        # Générer un ID aléatoire
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        data_with_id = f"<dataID={random_string}>{data}"

        # Sauvegarder les données dans un fichier (par exemple, 'OutServer.txt')
        with open('OutServer.txt', 'w') as file:
            file.write(data_with_id)

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

        return jsonify({'data': data}), 200

    except Exception as e:
        return jsonify({'message': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
