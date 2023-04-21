from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
     
    return render_template("login.html")

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'post':
        name = request.form['fullname'] 
        email = request.form['email']
        number = request.form['pnumber']
        c = request.form['course']

        details = [name,email,number,c]
        print(details)
        return render_template("course.html")
    
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
        return render_template("contact.html", =error)









if __name__ == "__main__":
    app.run(debug=True)