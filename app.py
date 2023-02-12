from flask import Flask , render_template ,request, session,redirect,url_for
import json

app = Flask(__name__)
app.secret_key = 'sfuffelklkelefmFELROERer6658'

def openfile():
    with open("db.json",'r',encoding='utf8') as f:
        return json.load(f)
    
def updatefile(name,etat,status):
    data = openfile()
    data[status][name]=int(etat)
    with open('db.json','w',encoding='utf8') as f:
        json.dump(data , f ,indent=4)
    

@app.route('/capteur')
def capteur():
    db =openfile()
    return render_template('capteur.html',db = db)

@app.route('/', methods=["GET","POST"])
def log():
    if request.method == 'POST':
        session['main'] = request.form.get('mail')
        session["pwd"] = request.form.get("pwd")
        if session['main'] == "admin" and session['pwd'] == "adm":
            return redirect(url_for("home"))
        else:
            return render_template('login.html' , alert = 'email or pwd incorrect')
    else:
        return render_template('login.html')

@app.route("/home")
def home():
    if session['main'] == "admin" and session['pwd'] == "adm":
        return render_template('home.html')
    else:
        return redirect(url_for("log"))
    

@app.route('/commad')
def commad():
    db =openfile()
    print(db)
    for key in db.keys():
        for elem in db[key]:
            if db[key][elem] == 1 and key == 'led':
               db[key][elem] = 'ON'
            elif db[key][elem]== 0 and key == 'led' :
               db[key][elem] = 'OFF'
            else:
                pass
    return render_template('commad.html', db = db ,etat ='etat')

@app.route("/api")
def api():
    d = openfile()
    print(d)
    return d

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/login/<name>/<etat>/<status>')
def login(name , etat,status):
    updatefile(name,etat,status)
    return ''
if __name__ == '__main__':
    app.run(debug=True)