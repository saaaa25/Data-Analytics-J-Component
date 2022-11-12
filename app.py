from flask import Flask, render_template, request
import pickle
import csv
import numpy as np

# submission = open('hotel_reviews.csv', 'w')
# sub_file = csv.writer(submission)
# sub_file.writerow(['Review'])

app = Flask(__name__)
model = pickle.load(open("hp.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():
    ff = [str(x) for x in request.form.values()]
    if ff[0] == "Bengaluru":
        ff[0] = 1
        ff[1] = int(ff[1])
        ff[2] = float(ff[2])
        ff[3] = float(ff[3])
    elif ff[0] == "Delhi":
        ff[0] = 2
        ff[1] = int(ff[1])
        ff[2] = float(ff[2])
        ff[3] = float(ff[3])
    elif ff[0] == "Goa":
        ff[0] = 3
        ff[1] = int(ff[1])
        ff[2] = float(ff[2])
        ff[3] = float(ff[3])
    else:
        ff[0] = 4
        ff[1] = int(ff[1])
        ff[2] = float(ff[2])
        ff[3] = float(ff[3])
    features = [np.array(ff)]
    result = model.predict(features)[0]
    return render_template("result.html",result = result)

@app.route("/feedback", methods = ["GET","POST"])
def feedback():
    review = ""
    if request.method == "POST":
        # getting input with name = fname in HTML form
        review = request.form.get("review")
        # sub_file.writerow([review])
        # submission.close()
    return render_template("feedback.html", msg = review)


if __name__ == "__main__":
    app.run(debug=True)