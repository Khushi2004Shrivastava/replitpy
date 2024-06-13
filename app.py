from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [{
    'id': 1,
    'title': 'Chemistry Lab Coat',
    'Availability': '5',
    'price': '500'
}, {
    'id': 2,
    'title': 'Engineering Drawing instruments',
    'Availability': '4',
    'price': 'free'
}, {
    'id': 3,
    'title': 'handwritten notes 1st sem',
    'price': '1000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', items=ITEMS, name='BEE')


@app.route("/api/items")
def list_items():
  return jsonify(ITEMS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
