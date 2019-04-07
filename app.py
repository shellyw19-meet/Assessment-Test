from flask import *
from database import *
import database
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/applicants', methods = ['GET', 'POST'])
def applicants():
	if request.method == 'GET':
		return render_template("home.html")
	else:
		name = request.form['name']
		age = request.form['age']
		subject = request.form['subject']
		add_applicant(name, age, subject)
		return redirect(url_for("applicants"), appl = database.get_all_applicants())

if __name__ == '__main__':
    app.run(debug=True)

