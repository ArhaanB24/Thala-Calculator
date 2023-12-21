from flask import Flask, render_template, request
import random 

app = Flask(__name__)
app.secret_key = "THALA"

@app.route("/",methods=["GET","POST"])
def home():
    numbers = ""
    final_val = None
    thala = False
    i = 0
    numbers = request.form.get("expression")
    check = []
    if numbers:
        numbers = numbers.strip()
        ops = ["*","+","-","/","%"]
        opsval = numbers.count(" ")
        i = 0
        while i!=(5**opsval):
            opslst = ""
            ans_val = ""
            for x in range(opsval):
                opslst += random.choice(ops)
            opslst += " "
            try:
                numlist = list(map(int,numbers.split(" ")))
            except ValueError:
                if len(numbers) == 7:
                    numlist = list(numbers)
                    for x in range(len(numlist)):
                        numlist[x]+="+"
                    final_val = "".join(numlist)
                    final_val = final_val[:-1]
                    thala = True
                    break
                else:
                    thala = False
                    final_val = "Not Thala"
                    break
            for x in range(len(numlist)):
                ans_val += str(numlist[x])+opslst[x]
            if opslst not in check:
                check.append(opslst)
                i+=1
                try:
                    if (eval(ans_val) == 7) or (eval(ans_val) == 7.0):
                        print("Thala For a Reason")
                        final_val = ans_val
                        thala = True
                except ZeroDivisionError:
                    pass
            else:
                pass
        if thala == False and i == 5**opsval:
            final_val = "Not Thala"
    else:
        numbers = ""
    return render_template("index.html",final_val=final_val,numbers=numbers,thala=thala)

if "__main__" == __name__:
    app.run(debug=True)