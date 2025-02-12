from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "I'm smart enough now to know I'm stupid. That's progress.",
    "That's pretty much a rule in electronics: You never get diodes right on the first try.",
    "Deadline-induced quality issues: a problem all over the galaxy.",
    "I clench every part of me that I know how to clench. It gives me a feeling of control. I'm doing something by aggressively doing nothing.",
    "All life needs is a chemical reaction that results in copies of the original catalyst.",
    "Got to love computers. They do all the thinking for you so you don't have to.",
    "One thing I learned back in my graduate school days: When you're stupid tired, accept that you're stupid tired. Don't try to solve things right then.",
    "It's a simple idea, but also stupid. Thing is, when stupid ideas work, they become genius ideas. We'll see which way this one falls.",
    "I am sad also. But we not be sad for long. You are scientist. I am engineer. Together we solve."
    
    
    
    
    
    
]

@app.route('/quotes', methods=['GET'])
def get_quote():
    return jsonify({"quote": random.choice(quotes)}), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == '__main__':
    app.run(debug=True)