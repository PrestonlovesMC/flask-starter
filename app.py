from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello", methods=["GET","POST"])
def example_form():
    if request.method == 'GET':
        return render_template('hello.html')
    elif request.method == 'POST':
        return render_template('greeting.html',
                               fullname=request.form['fullname'])

@app.route("/tip-calc", methods=["GET","POST"])
def tip_calc():
    if request.method == 'GET':
        return render_template('tip-calc.html')
    elif request.method == 'POST':
		tip_perc = float(request.form['tip-perc'])
		meal_price = float(request.form['meal-price'])
		tax_rate = float(request.form['tax-rate'])
		meal_plus_tax = meal_price + meal_price * tax_rate
		return render_template('tip-calc.html',
			tip_perc=tip_perc,
			meal_price=meal_price,
			tax_rate=tax_rate,
			meal_plus_tax=meal_plus_tax)
							   
@app.route('/my-new-page')
def my_new_function():
    print 'HELLO FROM MY NEW FUNCTION'
    return render_template('new-page.html')

if __name__ == "__main__":
    app.run(debug=True)
