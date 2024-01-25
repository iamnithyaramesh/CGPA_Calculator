from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)


def four_credit(grade):
    total=0
    if grade=='O':
        total=40
    elif grade=='A+':
        total=36
    elif grade=='A':
        total=32
    elif grade=='B+':
        total=28
    elif grade=='B':
        total=24
    elif grade=='C':
        total=20
    elif grade=='C+':
        total=16
    else:
        total=0

    return total
    
def three_credit(grade):
    total=0
    if grade in'Oo':
        total=30
    elif grade=='A+' or grade=='a+':
        total=27
    elif grade in'Aa':
        total=24
    elif grade=='B+' or grade=='b+':
        total=21
    elif grade=='Bb':
        total=18
    elif grade=='C+' or grade=='c+':
        total=15
    elif grade=='Cc':
        total=12
    else:
        total=0

    return total

def lab_credit(grade):

    total=0
    if grade in'Oo':
        total=15
    elif grade=='A+' or grade=='a+':
        total=13.5
    elif grade in'Aa':
        total=12
    elif grade=='B+' or grade=='b+':
        total=10.5
    elif grade=='Bb':
        total=9
    elif grade=='C+' or grade=='c+':
        total=7.5
    elif grade=='Cc':
        total=6
    else:
        total=0

    return total

def one_credit(grade):
    total=0
    if grade in'Oo':
        total=10
    elif grade=='A+' or grade=='a+':
        total=9
    elif grade in'Aa':
        total=8
    elif grade=='B+' or grade=='b+':
        total=7
    elif grade=='Bb':
        total=6
    elif grade=='C+' or grade=='c+':
        total=5
    elif grade=='Cc':
        total=4
    else:
        total=0

    return total


def cgpa_calculator3(maths, logic, com, p, db, u, tam, lab1, lab2):
    x = four_credit(maths) + three_credit(logic) + three_credit(com) + three_credit(p) + three_credit(db) + three_credit(u) + one_credit(tam) + lab_credit(lab1) + lab_credit(lab2)
    return round(x / 23,3)

def cgpa_calculator1(maths, phy, chem, eng, python,eg, tam, lab1, lab2):
    x = four_credit(maths) + three_credit(phy) + three_credit(chem) + three_credit(eng) + three_credit(python) + four_credit(eg) + one_credit(tam) + lab_credit(lab1) + lab_credit(lab2)
    return round(x / 24,3)



@app.route('/')
def index():
    return render_template('main_page.html')


@app.route('/semester_3')
def sem3():
    return render_template('sem3.html')


@app.route('/semester_1')
def sem1():
    return render_template('sem1.html')


@app.route('/calculate3', methods=['POST', 'GET'])
def calculate3():
    if request.method == 'POST':
        maths = request.form['maths']
        logic = request.form['logic']
        com = request.form['com']
        p = request.form['pdp']
        db = request.form['db']
        u = request.form['u']
        tam = request.form['tam']
        lab1 = request.form['lab1']
        lab2 = request.form['lab2']

        cgpa = cgpa_calculator3(maths, logic, com, p, db, u, tam, lab1, lab2)

        return redirect(url_for('result', cgpa=cgpa))
    
@app.route('/calculate1', methods=['POST', 'GET'])
def calculate1():
    if request.method == 'POST':
        math = request.form['math']
        phy = request.form['phy']
        chem = request.form['chem']
        eng = request.form['eng']
        python = request.form['python']
        eg = request.form['eg']
        tam = request.form['tam']
        py_lab = request.form['py_lab']
        phy_chem_lab = request.form['phy_chem_lab']

        cgpa = cgpa_calculator1(math, phy, chem, eng, python,eg,tam, py_lab, phy_chem_lab)

        return redirect(url_for('result', cgpa=cgpa))


@app.route('/result')
def result():
    
    cgpa = request.args.get('cgpa')

    return render_template('final_result.html', cgpa=cgpa)

def create_app():
   return app

if __name__ == '__main__':
    app.run(debug=False)