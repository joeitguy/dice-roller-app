import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

from flask import jsonify

@app.route('/roll')
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    is_double = die1 == die2
    return jsonify({
        'die1': die1,
        'die2': die2,
        'total': total,
        'is_double': is_double
    })
