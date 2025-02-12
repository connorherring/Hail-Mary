from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = {
"LOL": [    
    "I clench every part of me that I know how to clench. It gives me a feeling of control. I'm doing something by aggressively doing nothing.",
    "Got to love computers. They do all the thinking for you so you don't have to.",
    "One thing I learned back in my graduate school days: When you're stupid tired, accept that you're stupid tired. Don't try to solve things right then.",
    "It's a simple idea, but also stupid. Thing is, when stupid ideas work, they become genius ideas. We'll see which way this one falls.",
    "Fist me. Fist my bump",
    "They say hunger is the greatest seasoning",
    "Besides, if I had a nickel for every time I wanted to smack a kid’s parents for not teaching them even the most basic things…well…I’d have enough nickels to put in a sock and smack those parents with it."
    
],

"Awe": [
    "I am sad also. But we not be sad for long. You are scientist. I am engineer. Together we solve.",
    "Do you believe in God? I know it’s a personal question. I do. And I think He was pretty awesome to make relativity a thing, don’t you? The faster you go, the less time you experience. It’s like He’s inviting us to explore the universe, you know?"
],

"WTF":[
    "All life needs is a chemical reaction that results in copies of the original catalyst.",
    "Intelligence evolves to gives us an advantage over the other animals on our planet. But evolution is lazy. Once a problem is solved, the trait stops evolving.",
"*intentionally causing global warming by MELTING ANTARCTICA"
],

"Relatable":[
    "I'm smart enough now to know I'm stupid. That's progress.",
    "That's pretty much a rule in electronics: You never get diodes right on the first try.",
    "Deadline-induced quality issues: a problem all over the galaxy.",
    "Human beings have a remarkable ability to accept the abnormal and make it normal"
]

}


@app.route('/quotes', methods=['GET'])
def get_random_quote():
    """Returns a completely random quote from any category"""
    category = random.choice(list(quotes.keys()))  # Pick a random category
    quote = random.choice(quotes[category])
    return jsonify([category, quote])

@app.route('/quotes/<category>', methods=['GET'])
def get_quote_by_category(category):
    """Returns a random quote from a specific category"""
    if category not in quotes:
        return jsonify({"error": "Category not found"}), 404
    
    quote = random.choice(quotes[category])
    return jsonify([category, quote])

if __name__ == '__main__':
    app.run(debug=True)