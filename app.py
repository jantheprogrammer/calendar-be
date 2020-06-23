from flask import Flask, request, jsonify
from google_cal import events
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api', methods=['GET'])
def index():
    args = request.args

    # date of first event, when from_date is not provided, beginning of the year is taken
    from_date = args.get('from_date')
    if request.args.get('from_date') is None:
        from_date = '2020-01-01T00:00:00.0Z'

    # date of last event, when to_date is not provided, all up coming events are returned
    to_date = args.get('to_date')

    events_list = events.get_events(from_date=from_date, to_date=to_date)
    return jsonify(events_list)


if __name__ == '__main__':
    app.run(debug=True)
