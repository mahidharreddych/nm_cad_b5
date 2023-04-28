from flask import Flask, render_template, request, flash, redirect, url_for, session
import ibm_db
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

conn = ibm_db.connect("database = bludb; hostname = 2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud; port = 30756; uid = vts47207; password = g4O8mWodzytk1wMD;security=SSL; SSLServercertificate = DigiCertGlobalRootCA.crt ", " ", " ")

print("Connection Succesfull")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods = ['GET', 'POST'])
def login():
    global u_email
    if request.method == 'POST':
        u_email = request.form["uemail"]
        u_pass = request.form['upass']
        print("The emailid of the user : {} and password : {}". format(u_email, u_pass))
        sql  = "SELECT * from REGISTER_B5 WHERE EMAILID =  ? AND PASSWORD = ?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, u_email)
        ibm_db.bind_param(stmt, 2, u_pass)
        ibm_db.execute(stmt)
        info = ibm_db.fetch_assoc(stmt)
        print(info)
        if info : 
            session['id'] = True
            session['email'] = u_email

            return redirect(url_for("course"))
        else:
            msg_w = "Check the Email and Password you have entered"
            return render_template("login.html", msg_w = msg_w ) 
            
    return render_template("login.html")



@app.route("/register", methods=['GET', 'POST'])
def u_register():
    u_name = request.form['uname']
    u_email = request.form['uemail']
    u_pnumber = request.form['upnumber']
    u_pass = request.form['upass']
    print("Entered details for registation are : " ,u_name, u_email, u_pnumber, u_pass)
    sql  = "SELECT * from REGISTER_B5 WHERE EMAILID =  ? "
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, u_email)
    ibm_db.execute(stmt)
    info = ibm_db.fetch_assoc(stmt)
    print("info we got from the table : " , info)
    if info : 
        msg = "Your have been already registered : Kindly LOGIN"
        return render_template("login.html", msg = msg )
    else: 
        sql = "INSERT into REGISTER_B5 VALUES (?, ? , ? , ?)"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1 , u_name)
        ibm_db.bind_param(stmt, 2 , u_email)
        ibm_db.bind_param(stmt, 3 , u_pnumber)
        ibm_db.bind_param(stmt, 4 , u_pass)
        ibm_db.execute(stmt)
        msg_r = "your are successfully registered : kindly LOGIN"
        return render_template("login.html", msg_r = msg_r)
    



@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['fullname'] 
        email = request.form['email']
        number = request.form['pnumber']
        c = request.form['course']

        sql = "INSERT into contact_b5 VALUES (?, ? , ? , ?)"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1 , name)
        ibm_db.bind_param(stmt, 2 , email)
        ibm_db.bind_param(stmt, 3 , number)
        ibm_db.bind_param(stmt, 4 , c)
        ibm_db.execute(stmt)
        msg = "Thankyou for your Interest: Soon we will reachout to you."
        return render_template("contact.html", msg = msg)
    
    return render_template("contact.html")

@app.route("/course")
def course():
    return render_template("course.html")

@app.route("/file_type", methods = ['GET', 'POST'])
def upload_file():
    file = request.files['somefile']
    if file.filename != "NULL":
        fname = file.filename
        #fname = fname.strip(".pptx")
        print(fname) 
        file.save(fname + ".pdf")
        flash("File is Successfully uploaded") 
        return render_template("contact.html")
    else:
        error = "File is Not uploaded"
        return render_template("contact.html", error=error)

@app.route("/logout")
def logout():
    session.pop("id", None)
    session.pop("email", None)
    return render_template("index.html")








if __name__ == "__main__":
    app.run(debug=True)