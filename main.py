from flask import Flask, render_template, url_for
import requests

API_ENDPOINT = "https://api.npoint.io/f2ba3340fbfd2911d604"

app = Flask(__name__)

server_data = requests.get(API_ENDPOINT).json()

@app.route('/')
def starting():
    return render_template("/index.html", data = server_data)

@app.route('/about')
def about():
    return render_template("/about.html")

@app.route('/contact')
def contact():
    return render_template("/contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for data in server_data:
        if data['id'] == index:
            requested_post = data
    return render_template("post.html", post=requested_post)

if __name__=="__main__":
    app.run()

