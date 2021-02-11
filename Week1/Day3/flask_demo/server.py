from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hi, what's up? You have come to my page!</h1>"

@app.route('/shrek_info')
def shrek_info():

    kids_db = ["Winifred", "Mable", "Edith"]

    return f"""
    <h1> Shrek has 3 children! </h1>
    <ul>
        <li> {kids_db[0]} </li>
        <li> {kids_db[1]} </li>
        <li> {kids_db[2]} </li>
    </ul>
    """

@app.route('/greet/<greeting>/<int:num_times>')
def greetManyTimes(greeting, num_times):

    print(greeting)
    print(num_times)

    return render_template('index.html', greeting=greeting, num_times=num_times) 


if __name__ == "__main__":
    app.run(debug=True)