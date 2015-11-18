from flask import Flask
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
templates = Environment(loader=FileSystemLoader("/app/templates"))

@app.route("/")
def index():

    # get all the meals
    def parse_meal(line):
        words = line.strip().split(' ')
        return {
            "date": words[0],
            "dishes": ' '.join(words[1:]),
            }

    with open('/app/meals.txt', 'r') as mealsfile:
        meals = [parse_meal(m) for m in mealsfile.readlines()]

    # get all the ideas
    with open('/app/ideas.txt', 'r') as ideasfile:
        ideas = [i.strip() for i in ideasfile.readlines()]

    # render the template with the meals and ideas
    index_template = templates.get_template("index.html")
    return index_template.render(meals=meals, ideas=ideas)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
