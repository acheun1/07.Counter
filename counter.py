#Counter
#2018 10 02
#Cheung Anthony

# When you build this, please make sure that your program meets the following criteria:

from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key='as43df46asd3f4as4'

#our index route will handle the form
@app.route('/')
def index():
    if 'cnt' not in session:
        session['cnt']=0
    else:
        session['cnt']=session['cnt']+1
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)


