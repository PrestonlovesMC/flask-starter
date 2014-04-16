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
        tip_perc = float(request.form.get('tip-perc'))
        meal_price = float(request.form.get('meal-price'))
        tax_rate = float(request.form.get('tax-rate'))
        meal_plus_tax = meal_price + meal_price * tax_rate
        meal_plus_tip = meal_plus_tax + meal_plus_tax * tip_perc
        return render_template('tip-calc.html',
            tip_perc=tip_perc,
            meal_price=meal_price,
            tax_rate=tax_rate,
            meal_plus_tax=meal_plus_tax,
            meal_plus_tip=meal_plus_tip)
        
@app.route("/mad-libs", methods=["GET","POST"])
def mad_libs():
    if request.method == 'GET':
        return render_template('mad-libs.html')
    elif request.method == 'POST':
        return render_template('mad-libs.html',
                               past_time=request.form['past_time'],
                               name=request.form['name'],
                               car=request.form['car'])
@app.route("/mine-quiz", methods=["GET","POST"])
def mine_quiz():
    if request.method == 'GET':
        return render_template('mine-quiz.html')
    elif request.method == 'POST':
        question1 = request.form.get('question1')
        question2 = request.form.get('question2')
        question3 = request.form.get('question3')
        question4 = request.form.get('question4')
        number_correct = 0
        if question1 == 'false':
            number_correct = number_correct + 1
        if question2 == 'true':
            number_correct = number_correct + 1 
        if question3 == 'true':
            number_correct = number_correct + 1      
        if question4 == 'false':
            number_correct = number_correct + 1   
        print question1, question2, question3, question4
        perc_correct = 100 * number_correct / 4
        return render_template('mine-quiz.html',
                                number_correct=number_correct,
                                perc_correct=perc_correct)
@app.route('/my-new-page')
def my_new_function():
    print 'HELLO FROM PRESTONS WEB APPLICATION'
    return render_template('new-page.html')

if __name__ == "__main__":
    app.run(debug=True)
