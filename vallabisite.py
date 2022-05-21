from flask import Flask, render_template ,request,url_for,redirect
from flask_mysqldb import MySQL
import smtplib


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "vallabi"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)




@app.route('/',methods=["GET","POST"])
def home():
    if request.method == "POST":
        n1 = request.form['names']
        pn = request.form['phonenumbers']
        em = request.form["emails"]
        desc = request.form["descs"]
        con = mysql.connection.cursor()
        sql = "insert into d1(name,phonenumber,email,description1) values(%s,%s,%s,%s)"
        con.execute(sql,[n1,pn,em,desc])
        mysql.connection.commit()
        con.close()

    return render_template('home.html')

@app.route('/service')
def menues():
    return render_template('service.html')

@app.route('/contact')
def contacts():
    return render_template('contact.html')






    


if (__name__ == '__main__'):
    app.run(debug=True)