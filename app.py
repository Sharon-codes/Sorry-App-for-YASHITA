# app.py
from flask import Flask, render_template
import random

app = Flask(__name__)

SORRY_MESSAGES = [
    "I'm so sorry, I'll be your personal clown for a week 🤡",
    "Begging for forgiveness with maximum drama and zero chill 🎭",
    "If sorry were a competitive sport, I'd be Olympic champion 🏅",
    "Prepare for the most extra apology in friendship history 💥",
    "My bad game is so strong, it's almost art 🎨",
    "Imagine the most annoying apology. I'm about to one-up that. 😈"
]

GIFS = [
    'https://media.giphy.com/media/l2QEgDpnZACjTlRPW/giphy.gif',
    'https://media.giphy.com/media/3o6Zt4HU9uwXmXSAuI/giphy.gif',
    'https://media.giphy.com/media/l0HlBO7yB4Fw5Bon6/giphy.gif'
]

@app.route('/')
def sorry_app():
    random_message = random.choice(SORRY_MESSAGES)
    random_gif = random.choice(GIFS)
    return render_template('sorry.html', message=random_message, gif=random_gif)

if __name__ == '__main__':
    app.run(debug=True)