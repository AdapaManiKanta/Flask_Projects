#Imports
from flask import Flask , render_template


#My app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)