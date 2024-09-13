from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        try:
            prelim_grade = float(request.form['prelim_grade'])
            # Simple example computation: let's just return the prelim grade
            result = f'Prelim Grade: {prelim_grade}'
        except ValueError:
            error = 'Invalid input. Please enter a numeric value.'
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
