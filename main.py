from flask import Flask, render_template, request
import random 

app = Flask(__name__)
app.secret_key = "THALA"

@app.route("/",methods=["GET","POST"])
def home():
    numbers = ""
    final_val = None
    numbers = request.form.get("expression")
    if numbers:
        i = 0
        while True:
            ans_val = ""
            ops = ["*","+","-","/","%"]
            opsval = numbers.count(" ")
            opslst = ""
            for x in range(opsval):
                opslst += random.choice(ops)
            opslst += " "
            numlist = list(map(int,numbers.split(" ")))
            for x in range(len(numlist)):
                ans_val += str(numlist[x])+opslst[x]
            try:
                if (eval(ans_val) == 7) or (eval(ans_val) == 7.0):
                    print("Thala For a Reason")
                    final_val = ans_val
                    break
            except ZeroDivisionError:
                pass
            i+=1
            if (i == 100):
                print("Break")
                final_val == None
                break
    else:
        numbers = ""
    return render_template("index.html",final_val=final_val,numbers=numbers)

if "__main__" == __name__:
    app.run(debug=True)