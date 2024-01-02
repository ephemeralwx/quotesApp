from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Organizing the quotes into three categories: Personal Development, Entrepreneurship, and Resilience

personal_development_quotes = [
    "The easiest way to change your behavior is to change your surroundings. - Alex Hormozi",
    "We pay for every lesson with either time or money. And we use the currency we value least. - Alex Hormozi",
    "Wanna know how long it takes to get over disappointment? As long as you decide it takes. - Alex Hormozi",
    "Who you compare yourself to dictates who you become. - Alex Hormozi",
    "It’s not about what they’re doing that you aren’t, it’s about what they aren’t doing that you are. - Alex Hormozi",
    "You are in danger of living a life so comfortable and soft, that you will die without ever realizing your true potential. - David Goggins",
    "No one is going to come help you. No one's coming to save you. - David Goggins",
    "The most important conversations you’ll ever have are the ones you’ll have with yourself. - David Goggins",
    "Denial is the ultimate comfort zone. - David Goggins",
    "Everything in life is a mind game! - David Goggins",
    # ... and more
]

entrepreneurship_quotes = [
    "The only way that you can make the most money is to provide an exceptional valued service and charge a ton of money for it. - Alex Hormozi",
    "I’ll give you the first rule of entrepreneurship; use what you have. - Alex Hormozi",
    "Scarcity is a function of quantity. Urgency is a function of time. - Alex Hormozi",
    "Multi-tasking is like balancing spinning plates. Sure, it sounds exciting but you’ll never unlock the compounding effects of narrowly focused attention. - Alex Hormozi",
    "In my opinion, the most important thing for an entrepreneur is to create more space to do deeper work. - Alex Hormozi",
    "Our culture has become hooked on the quick-fix, the life hack, efficiency. - David Goggins",
    "It's a lot more than mind over matter. It takes relentless self discipline to schedule suffering into your day, every day. - David Goggins",
    "We’re either getting better or we’re getting worse. - David Goggins",
    "Be more than motivated, be more than driven, become literally obsessed to the point where people think you're fucking nuts. - David Goggins",
    "We live in a world with a lot of insecure, jealous people. Some of them are our best friends. They are blood relatives. - David Goggins",
    # ... and more
]

resilience_quotes = [
    "If you’re willing to embrace discomfort in the short-term for prosperity in the long-term, then nothing will be able to stop you. - Alex Hormozi",
    "The pain you feel today builds the strength you have tomorrow. - Alex Hormozi",
    "If you have trouble being productive or doing the things you need to do to reach your goals, then I would consider entering a season of no. - Alex Hormozi",
    "Sometimes you have to let other people’s dreams for your life die so that yours can live. - Alex Hormozi",
    "Winners win. The only thing that separates people who don’t win from those who do is the ones who try. - Alex Hormozi",
    "It won’t always go your way, so you can’t get trapped in this idea that just because you’ve imagined a possibility for yourself that you somehow deserve it. - David Goggins",
    "I thought I’d solved a problem when really I was creating new ones by taking the path of least resistance. - David Goggins",
    "I don't stop when I'm tired. I stop when I'm done - David Goggins",
    "The reason it’s important to push hardest when you     want to quit the most is because it helps you callous your mind. - David Goggins",
    "Pain unlocks a secret doorway in the mind, one that leads to both peak performance, and beautiful silence. - David Goggins",
    # ... and more
]




@app.route('/get_quote', methods=['GET'])
def get_quote():
    # Extract boolean variables from the request
    resilience = request.args.get('resilience', default='false').lower() == 'true'
    entrepreneurship = request.args.get('entrepreneurship', default='false').lower() == 'true'
    personal_development = request.args.get('personalDevelopment', default='false').lower() == 'true'

    # Create a pool of quotes based on selected topics
    quotes_pool = []
    if resilience:
        quotes_pool.extend(resilience_quotes)
    if entrepreneurship:
        quotes_pool.extend(entrepreneurship_quotes)
    if personal_development:
        quotes_pool.extend(personal_development_quotes)

    # Check if no topics are selected
    if not quotes_pool:
        return jsonify({"quote": "No topics selected", "author": "No topics selected", "topic": "No topics selected"})


    # Select a random quote
    selected_quote = random.choice(quotes_pool)
    quote, author = selected_quote.split(" - ")

    # Determine the topic of the selected quote
    if selected_quote in personal_development_quotes:
        topic = "Personal Development"
    elif selected_quote in entrepreneurship_quotes:
        topic = "Entrepreneurship"
    else:
        topic = "Resilience"

    # Return the selected quote with its details
    return jsonify({"quote": quote, "author": author, "topic": topic})

if __name__ == '__main__':
    app.run(debug=True)
