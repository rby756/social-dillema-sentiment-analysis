from flask import Flask, render_template, request
from preprocessing import clean_text,deEmojify

import pickle

app = Flask(__name__)
preprocessing=pickle.load(open('preprocessing.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
	return render_template('index.html')


@app.route("/predict/", methods=['GET', 'POST'])
def prediction():
	if request.method=='POST':
		text=request.form['tweet']
		text=[deEmojify(text)]
		text=[clean_text(text)]
		print(text)
		predict=model.predict(text)
		print(predict)
		return render_template("result.html", predict=predict)

		

# A way to check if the file is being run as a script or imported as a module.
if __name__=='__main__':
	app.run(debug=True)