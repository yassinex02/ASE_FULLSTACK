from flask import Flask, request, render_template_string
app = Flask(__name__)


@app.route('/')
def home():
    return render_template_string(open('templates/index.html').read())


@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    return render_template_string(f'<h1>You entered: {user_input}</h1>')


if __name__ == '__main__':
    app.run()
