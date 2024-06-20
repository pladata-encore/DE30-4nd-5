from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
    <html>
    <head>
        <title>Movie Recommendation System</title>
    </head>
    <body>
        <h1>Welcome to Movie Recommendation System!</h1>
        <p>Click the button below to get a movie recommendation:</p>
        <form action="/recommend" method="get">
            <button type="submit">Get Recommendation</button>
        </form>
    </body>
    </html>
    '''

@app.route('/recommend')
def recommend_movie():
    movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump']
    recommended_movie = random.choice(movies)
    return jsonify({'movie': recommended_movie})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
