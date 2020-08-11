from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<string:path>')
def load_page(path):
	return render_template(path, title="My Website")

@app.route('/submit_form', methods = ["POST", "GET"])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thx.html')
		except:
			return 'Did not save to database!'
	else:
		return 'Something went wrong! Try again!'

def write_to_file(data):
	with open('database.txt', mode="a") as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		database.write(f'{email},{subject},{message}\n')

def write_to_csv(data):
	with open('database.csv', mode="a", newline='') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email, subject, message])