import os, dotenv
from flask import Flask, render_template
app = Flask(__name__)
dotenv.load_dotenv()

color = os.environ.get('APP_COLOR')
@app.route("/")
def main():
    print(color)
    return render_template('hello.html', color=color)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")



