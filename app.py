from flask import Flask, render_template
from scrape_imdb.imdb_scrape import get_movies_paged

app = Flask(__name__, template_folder='templates')


@app.route('/')
def function():
    my_data = get_movies_paged()
    return render_template('index.html', data=my_data)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
