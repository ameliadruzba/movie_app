'''klucz_api = https://api.themoviedb.org/3/movie/550?api_key=806bd346aad5cb1aee4b241382a93c85'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = ['krasnal']
    return render_template("index.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)