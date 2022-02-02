from flask import Flask, request, render_template

import pandas as pd
import joblib

model = joblib.load(open("model2.pkl","rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return "flask server is running"

@app.route("/api", methods = ["GET", "POST"])
def api():
    if request.method == "GET":
        return "welcomte my API server"
    if request.method == "POST":
        data = request.json
        df = pd.DataFrame(data)
        res = model.predict(df.values)
        return {"response":str(res)}


if __name__ == "__main__":
    app.run(debug=True, port=81)

if __name__ == '__main__':
   app.run(host="0.0.0.0",port=5000, threaded=True)