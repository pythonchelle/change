from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/money', methods=['post'])
def money():
    amount = request.form['amount']
    return render_template('money.html', amount=amount)

if __name__ == '__main__':
    app.run()
