from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_message', methods=['POST'])
def set_message():
    # get data from POST request
    receiver_host = request.form['receiver_host']
    receiever_name = request.form['receiever_name']
    sender_name = request.form['sender_name']
    type = request.form['type']
    color = request.form['color']
    content = request.form['content']
    
    # dictionary with data
    data = {
        "type": type,
        "color": color,
        "content": content,
        "sender_name": sender_name,
        "receiever_name": receiever_name
    }

    # convert dictionary to JSON data
    json_data = json.dumps(data)
    print(json_data)
    print(receiver_host)
    # set HTTP headers to application/json
    headers = {'Content-Type': 'application/json'}
    # send POST request to host endpoint with JSON data and headers
    response = requests.post('http://' + receiver_host + '/set_message', json=json_data, headers=headers)
    print(response.text)
    #print(response.json())
    return jsonify({'status': 'Message set', 'type': type, 'color': color, 'message': content, 'sender_name': sender_name, 'sender_host': request.host, 'receiever_name': receiever_name, 'receiver_host': receiver_host})

if __name__ == '__main__':
    app.run(port=3000)
