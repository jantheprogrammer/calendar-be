from flask import Flask, request, render_template, jsonify
from google_cal import events
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['GET'])
def index():
    events_list = events.get_events()
    return jsonify(events_list)


if __name__ == '__main__':
    app.run(debug=True)
