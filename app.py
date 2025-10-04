from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

pick_up_lines = {
    "cheesy": [
        "Are you a magician? Because whenever I look at you, everyone else disappears.",
        "Do you have a name or can I call you mine?",
        "Are you a loan? Because you have my interest.",
        "Do you believe in love at first sight—or should I walk by again?",
        "If you were a vegetable, you'd be a cute-cumber!",
        "Are you a parking ticket? Because you've got 'FINE' written all over you.",
        "Are you a camera? Every time I look at you, I smile.",
        "Is your name Google? Because you've got everything I'm searching for.",
        "Do you have a Band-Aid? I just scraped my knee falling for you.",
        "Are you a light bulb? Because you brighten up my day!",
        "Excuse me, but I think you dropped something: my jaw.",
        "Are you a snowstorm? Because you make my heart race.",
        "If beauty were time, you'd be eternity.",
        "Are you my Wi-Fi? Because I feel a connection.",
        "You must be tired because you've been running through my mind all day.",
        "Are you a cupcake? Because you're sweet and irresistible.",
        "If you were a fruit, you'd be a fine-apple.",
        "Are you a star? Because your beauty lights up the night.",
        "Do you have a compass? I keep getting lost in your eyes.",
        "Are you chocolate? Because you make life sweeter.",
        "Are you a rainbow? Because you bring color to my world.",
        "You must be a magician because every time I look at you, everyone else disappears.",
        "Are you a dictionary? Because you add meaning to my life.",
        "Are you sugar? Because you make life sweet.",
        "Are you a sunrise? Because you brighten my morning."
    ],

    "clever": [
        "Are you Wi-Fi? Because I'm feeling a connection.",
        "Do you like Star Wars? Because Yoda one for me!",
        "Are you French? Because 'Eiffel' for you.",
        "If we were words in a book, we'd be on the same page.",
        "Are you an algorithm? Because you complete my function.",
        "Do you like science? Because I've got my ion you.",
        "Are you a software update? Because whenever I see you, I improve.",
        "Are you a black hole? Because you're irresistible.",
        "Are you a keyboard? Because you're my type.",
        "Are you a puzzle? Because I can't figure out life without you.",
        "Are you a thesaurus? Because you're giving meaning to my words.",
        "If we were programming languages, we'd be Python and JavaScript—perfectly compatible.",
        "Are you parallel lines? Because no one else compares to you.",
        "Are you a smart contract? Because I'm committed to you.",
        "Are you a logic gate? Because you control my heart.",
        "Are you a telescope? Because you make the universe clearer.",
        "Are you encryption? Because you've locked up my heart.",
        "Are you a loop? Because I could go on with you forever.",
        "Are you a compiler? Because you make sense of my code.",
        "Are you a function? Because you make my life return joy.",
        "Are you a database? Because you store all my love.",
        "Are you a signal? Because you're sending waves of love my way.",
        "Are you a cloud server? Because you've got me stored in your heart.",
        "Are you an API? Because I want to connect with you.",
        "Are you a variable? Because you change my world."
    ],

    "nerdy": [
        "Are you made of copper and tellurium? Because you're Cu-Te.",
        "Are you a 45-degree angle? Because you're acute-y!",
        "Are you a carbon sample? Because I want to date you.",
        "Are you a neuron? Because you make my heart fire.",
        "Are you a quantum particle? Because whenever I look at you, I'm uncertain about everything else.",
        "Are you a binary tree? Because I feel a connection.",
        "Are you Pi? Because you're irrationally attractive.",
        "Are you a compiler? Because every time I see you, I feel complete.",
        "Are you a proton? Because you're positively charming.",
        "Are you a quark? Because you're elementary to my happiness.",
        "Are you a string theory? Because you tie everything together.",
        "Are you a capacitor? Because you store my love.",
        "Are you an equation? Because you make my heart balance.",
        "Are you a black hole? Because I'm drawn to you.",
        "Are you a photon? Because you light up my life.",
        "Are you a Higgs boson? Because you give my heart mass.",
        "Are you a neuron? Because we have a strong connection.",
        "Are you a circuit? Because you complete me.",
        "Are you a derivative? Because you make my heart rate change.",
        "Are you a matrix? Because you transform my world.",
        "Are you an atom? Because you're the center of my universe.",
        "Are you a proton and neutron? Because you make me feel balanced.",
        "Are you a magnet? Because you attract me irresistibly.",
        "Are you a compiler error? Because you make me stop in my tracks.",
        "Are you an electron? Because you're making my heart spin."
    ]
}


used_lines = {
    "cheesy": set(),
    "clever": set(),
    "nerdy": set()
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    category = request.args.get('category', 'cheesy')
    lines = pick_up_lines.get(category, pick_up_lines['cheesy'])
    available_lines = list(set(lines) - used_lines[category])

    if not available_lines:
        used_lines[category].clear()
        available_lines = lines
    
    line = random.choice(available_lines)
    used_lines[category].add(line)

    return jsonify({'line': line})

if __name__ == "__main__":
    app.run(debug=True)
