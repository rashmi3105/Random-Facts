from flask import Flask, request, jsonify, make_response
import random

app = Flask(__name__)

fact_list = ["Dogs sniff good smells with their left nostril.",
             "There were active volcanoes on the moon when dinosaurs were alive", "Bananas grow upside-down",
             "Only a quarter of the Sahara Desert is sandy.", "T. S. Eliot wore green makeup",
             "The Terminator script was sold for $1.", "Boars wash their food.",
             "Baseball umpires used to sit in rocking chairs.",
             "The French-language Scrabble World Champion doesn’t speak French.",
             "A woman called the police when her ice cream didn’t have enough sprinkles.",
             "The British Empire was the largest empire in world history.", "The first stroller was pulled by a goat.",
             "170-year-old bottles of champagne were found at the bottom of the Baltic Sea.",
             "Nikola Tesla hated pearls.",
             "Pregnancy tests date back to 1350 BCE. Egyptian women urinated on wheat and barley seeds to determine if they were pregnant or not.",
             "Bananas glow blue under black lights.", "Bees can make colored honey.",
             "Wimbledon tennis balls are kept at 68 degrees Fahrenheit.", "Adult cats are lactose intolerant.",
             "Sloths have more neck bones than giraffes.", "Bees can fly higher than Mount Everest.",
             "Ancient Egyptians used dead mice to ease toothaches."]


@app.route('/random_fact', methods=['GET'])
def random_fact():
    fact = random.choice(fact_list)
    return make_response(jsonify(fact), 200)


if __name__ == "__main__":
    app.run(debug=True)
