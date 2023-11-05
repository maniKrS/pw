from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input_form():
    user_input = None

    if request.method == 'POST':
        user_input = request.form.get('user_input')

    return render_template('input.html', user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
