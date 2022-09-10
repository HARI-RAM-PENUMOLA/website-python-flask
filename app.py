from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Web developer',
    'location': 'Hyderabad',
}]


@app.route("/")
def hello():
    return render_template('home.html', jobs=JOBS, company_name='Hash')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
