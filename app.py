from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/coin/")
def coin():
    return render_template("coin.html", coin = random.choice(["Head","Tails"]))
    
@app.route("/pick/<choice1>/<choice2>")
def pick(choice1, choice2):
    return render_template("pick.html", pick=random.choice([choice1,choice2]))

@app.route("/age/<year>")
def age(year):
    return render_template("age.html",age=2026-int(year))

@app.route("/magic/")
def magic():
    return render_template("magic8airball.html",magic=random.choice(["Definitaly", "Yes", "50/50", "No", "NO"]) ) 
   
@app.route("/fizzbuzz/")
def fizzbuzz():
    result=[]
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
           result.append("Buzz")

        else:
            result.append(n)
        
    return render_template("fizzbuzz.html", result=result)

@app.route("/shout/<word>")
def shout(word):
 

    return render_template("shout.html", word=word.upper())

@app.route("/grade/<grade>")
def grade(grade):
    res=[]
    if int(grade) >= 90:
        res.append("A")
    if int(grade) >= 85 and int(grade) <90:
        res.append("B")
    if int(grade) >= 71 and int(grade) < 85:
        res.append("C")
    if int(grade) < 71 and int(grade) >=60:
        res.append("D")
    if int(grade)<60:
        res.append("F")

    return render_template("grade.html", res=res)


if __name__ == "__main__":
    app.run(debug=True)
