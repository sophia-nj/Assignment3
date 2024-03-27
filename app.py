from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'student_number': 'YourStudentNumberHere'})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Example fulfillment logic
    return jsonify({'fulfillmentText': 'This is a response from your webhook!'})

if __name__ == '__main__':
    app.run(debug=True)
