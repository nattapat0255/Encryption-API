from flask import Flask, request, jsonify
from aes_cipher import AESCipher
from os import urandom
key = urandom(16)
aes = AESCipher(key)

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
  try:
    data = request.get_json()
    for i in range(len(data['data'])):
      encrypt_data = aes.encrypt(data['data'][i]['text'])
      data['data'][i] = {"encrpyted" : encrypt_data}
    return jsonify(data)
  except:
    return jsonify({"message": "Something went wrong, please try again."}),400

@app.route('/decrypt', methods=['POST'])
def decrypt():
  try:
    data = request.get_json()
    for i in range(len(data['data'])):
      decrypt_data = aes.decrypt(data['data'][i]['encrpyted'])
      print(decrypt_data)
      data['data'][i] = {"text" : decrypt_data}
    return jsonify(data)
  except:
    return jsonify({"message": "Something went wrong, please try again."}),400
