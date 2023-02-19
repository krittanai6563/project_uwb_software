from flask import Flask,session, render_template, request, redirect
import pyrebase


app = Flask(__name__)





config = {
    'apiKey': "AIzaSyC2l21YBFXUdqz61ukwaRXcEynt7t32C30",
    'authDomain': "projectuwb-27b59.firebaseapp.com",
    'databaseURL': "https://projectuwb-27b59-default-rtdb.firebaseio.com",
    'projectId': "projectuwb-27b59",
    'storageBucket': "projectuwb-27b59.appspot.com",
    'messagingSenderId': "436204132556",
    'appId': "1:436204132556:web:045ca6a919b9f886454a69",
    'measurementId': "G-574YC9RVV3",
    'daabaseURL' : ''
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app.secret_key ='secret'





            #   data: [{ { % for dt in chart_data % } {{dt}}, {% endfor %} 
# data = [{
#    'x': 20,
#    'y': 30,
#    'r': 15
#     }, 
#     {
#    'x': 20,
#    'y': 30,
#    'r': 15
#     }]

@app.route('/', methods=['POST','GET'])
def index():
    # if ('user' in session):
    #     return 'Hi , {}' .format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            session['user'] = email
        
            return render_template("index.html")  
        except:
            return 'รหัสผ่านไม่ถูกต้อง'


    return render_template("Login.html")

    # chart_data = data
    # return render_template("index.html", chart_data = chart_data)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


@app.route('/index')
def main():


    Tag_UWB = { "x": 0, "y": 0, "r": 20.0 }
    Anchor_UWB =[{ "x": 0, "y": 10, "r": 20},
        { "x": 10, "y": 10, "r": 20},
        { "x": 5, "y": 0, "r": 20 },]
    
    data = getAnchor()
    r1,r2,r3 = data[0],data[1],data[2]

    anc_1 = Anchor_UWB[0]
    anc_2 = Anchor_UWB[1]
    anc_3 = Anchor_UWB[2]
    st =  str(r1) + " " + str(r2) + " " + str(r3)
    Tag_UWB["x"],Tag_UWB["y"] = trackPhone(anc_1["x"],anc_1["y"],r1, anc_2["x"],anc_2["y"],r2, anc_3["x"],anc_3["y"],r3)
  
    return render_template("index.html" ,Tag1=[Tag_UWB], Anchor1=Anchor_UWB , getAnchor= st)  


def trackPhone(x1,y1,r1,x2,y2,r2,x3,y3,r3):
    A = 2*x2 - 2*x1
    B = 2*y2 - 2*y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2*x3 - 2*x2
    E = 2*y3 - 2*y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)
    return x,y

@app.route('/location_history')
def location_history():
    Tag = [{ "x": 5.3, "y": 16.5, "r": 30.0 },
        { "x": 6.4, "y": 13.5, "r": 4.72},
        { "x": 6.4, "y": 11.1, "r": 0.84 },]
    

    Anchor = [{ "x": 10, "y": 25, "r": 10},
        { "x": 50, "y": 25, "r": 10},
        { "x": 30, "y": 0, "r": 10 },]
    

    chart_Tag = Tag
    chart_Anchor = Anchor
    return render_template("location_history.html", chart_Tag = chart_Tag, chart_Anchor=chart_Anchor)

R = 10

def getAnchor():
    anchor1  = db.child("esp32").child("json").child("Anchor1").get().val()
    size1 = len(anchor1)
    lastData1 = anchor1[size1-1]

    anchor2  = db.child("esp32").child("json").child("Anchor2").get().val()
    size2 = len(anchor2)
    lastData2 = anchor2[size1-1]

    anchor3  = db.child("esp32").child("json").child("Anchor3").get().val()
    size3 = len(anchor3)
    lastData3 = anchor3[size1-1]

    return [lastData1,lastData2,lastData3]

@app.route('/add_user', methods=['GET' , 'POST'])
def add_user():

    user = db.child("user").get()
    to = user.val()

    if request.method == "POST":
        if request.form['submit'] == 'บันทึก' :
           
     
           name = request.form['name']
           Email = request.form['Email']
           tel = request.form['tel']
           numbertag = request.form['numbertag']

           db.child("user").push([name , Email, tel , numbertag])

           return render_template('Add_user.html', t = to.values())
        
    return render_template('Add_user.html', t = to.values())
   
    return render_template("Add_user.html")    


if __name__ == "__main__":
    app.run(debug=True)