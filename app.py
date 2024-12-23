from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Ciao, Flask è in esecuzione!"

if __name__ == "__main__":
    app.run(debug=True)