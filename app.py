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
  
    return render_template("index.html")  

@app.route('/location_history')
def location_history():
    Tag = [{ "x": 5.3, "y": 16.5, "r": 30.0 },
        { "x": 6.4, "y": 13.5, "r": 4.72},
        { "x": 6.4, "y": 11.1, "r": 0.84 },]
    

    Anchor = [{ "x": 5, "y": 16.5, "r": 7},
        { "x": 6, "y": 13, "r": 4},
        { "x": 6, "y": 11, "r": 8 },]
    

    chart_Tag = Tag
    chart_Anchor = Anchor
    return render_template("location_history.html", chart_Tag = chart_Tag, chart_Anchor=chart_Anchor)



@app.route('/add_user', methods=['GET' , 'POST'])
def add_user():
    if request.method == "POST":
        if request.form['submit'] == 'บันทึก' :
           
     
           name = request.form['name']
           Email = request.form['Email']
           tel = request.form['tel']
           numbertag = request.form['numbertag']

           db.child("user").push([name , Email, tel , numbertag])
           user = db.child("user").get()
           to = user.val()
           return render_template('Add_user.html', t = to.values())
        
    
   
    return render_template("Add_user.html")    


if __name__ == "__main__":
    app.run(debug=True)