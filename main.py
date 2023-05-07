import pandas as pd
import pickle
from flask import Flask,render_template,request,jsonify

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

def predict(page_views,	fpl_value,	fpl_sel,	fpl_points,	big_club):
    x = pd.DataFrame([])
    x[["page_views",	"fpl_value",	"fpl_sel",	"fpl_points",	"big_club"]] = [[page_views,	fpl_value,	fpl_sel,	fpl_points,	big_club]]
    model = pickle.load(open("predictPrice.pkl", "rb"))
    price = model.predict(x)
    return price[0]
    
    # return render_template("index.html")

if __name__=="__main__":
    app.run("0.0.0.0",port = 5000, debug=True)