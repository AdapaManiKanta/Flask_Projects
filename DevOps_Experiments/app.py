from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Store the user's data in a file or database here (currently skipped)
        
        return render_template("success.html")
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
