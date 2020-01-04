from flask import Flask, request, render_template
from google_cal import events

app = Flask(__name__)


@app.route('/')
def index():
    events_list = events.get_events()
    return render_template('index.html', events=events_list)


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return 'posted'
#     else:
#         return 'get'


if __name__ == '__main__':
    app.run(debug=True)
