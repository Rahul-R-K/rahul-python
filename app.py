from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [{
  'id': '1',
  'tittle': 'Manual Testing',
  'place': 'Chennai'
}, {
  'id': '2',
  'tittle': 'Automation Testing',
  'place': 'USA'
}, {
  'id': '1',
  'tittle': 'Front End',
  'place': 'Delhi'
}, {
  'id': '1',
  'tittle': 'Back End',
  'place': 'Mumbai'
}]


@app.route("/")
def Host():
  return render_template('home.html', jobs=JOBS, company='Jovian Carrer')


@app.route("/api/jobs")
def joblist():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
