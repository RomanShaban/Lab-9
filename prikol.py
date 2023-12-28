from flask import Flask, render_template

app= Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT']
@app.route("/")
def cait():
    return render_template("cait.html")
    
if __name__ == "__main__":
    app.run(debug=True)
