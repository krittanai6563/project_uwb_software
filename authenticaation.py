import pyrebase

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
db = firebase.database()

# db.child("user").push({"name":"krittanai"})
db.child("user").update({"name":"krittanai1"})









# auth = firebase.auth()

# email = 'test@gmail.com'
# password = '123456'

# # user = auth.create_user_with_email_and_password(email, password)
# # print(user)

# user = auth.sign_in_with_email_and_password(email, password)

# # info = auth.get_account_info(user['idToken'])
# # print(info)


# # auth.send_email_verification(user['idToken'])

# auth.send_password_reset_email(email)