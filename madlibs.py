from random import sample, randint

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    num_of_compliments = randint(1, len(AWESOMENESS))

    compliments = sample(AWESOMENESS, num_of_compliments)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Get user's response to the yes or no question on the 'would you like to
    play a game?' form.
    """

    response = request.args.get("wantstoplay")
    if response == "no":
        return render_template("goodbye.html")
    if response == "yes":
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """renders template madlib.html, filling in info provided by user into a
    MadLibs-style story.
    """
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    return render_template("madlib.html",
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
