from flask import Flask,render_template,request,redirect
import mysql.connector

app=Flask(__name__)

@app.route('/')
def Home():
    return render_template('register.html')

# route for collecting data from form and insert into db

@app.route('/register', methods=['POST'])
def StudentRegister():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Poojasri@1234',
        database='studentmng'

    )

    #collecting data from form:
    sid=int(request.form['sid'])
    sname=request.form['sname']
    sbranch=request.form['sbranch']
    smarks=int(request.form['smarks'])
    spno=request.form['spno']

    # create cursor object, execute quaries and commit
    cursor=mydb.cursor()
    cursor.execute("insert into studentmngt(sid,sname,sbranch,smarks,spno) values(%s,%s,%s,%s,%s)",(sid,sname,sbranch,smarks,spno))
    mydb.commit()
    cursor.close()
    return f"Student Registered Successfully! <br><br> <a href='/'>New Registration</a> <br><br> <a href='/view'>View Student registered Data</a>"

# route for view/send data to html page
@app.route('/view')
def SendData():
    mydb=mysql.connector.connect(
        host="localhost",
        user='root',
        password='Poojasri@1234',
        database='studentmng'
    )

    #create cursor object, execute quaries and commit
    cursor=mydb.cursor()
    cursor.execute("select * from studentmngt")
    data=cursor.fetchall()
    cursor.close()
    return render_template('view.html',students=data)

# route for delete student
@app.route('/delete/<sid>')
def DeleteStudent(sid):
    mydb=mysql.connector.connect(
        host="localhost",
        user='root',
        password='Poojasri@1234',
        database='studentmng'
    )

    #create cursor object, execute queries and commit
    cursor=mydb.cursor()
    cursor.execute("Delete From studentmngt where sid=%s",(sid,))
    mydb.commit()
    cursor.close()
    return redirect('/view')

# route for edit student
@app.route('/edit/<sid>')
def edit(sid):
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Poojasri@1234',
        database='studentmng'
    )

    #create cursor object, execute queries and commit
    cursor=mydb.cursor()
    cursor.execute("select * from studentmngt where sid=%s ",(sid,))
    student=cursor.fetchone()
    cursor.close()
    return render_template('edit.html',student=student)

#route for update student(save changes)
@app.route('/update',methods=['POST'])
def UpdateStudent():
    mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Poojasri@1234',
        database='studentmng'
    )

    sid=int(request.form['sid'])
    sname=request.form['sname']
    sbranch=request.form['sbranch']
    smarks=int(request.form['smarks'])
    spno=request.form['spno']

    #create cursor object, execute queries and commit
    cursor=mydb.cursor()
    cursor.execute("update studentmngt set sname=%s, sbranch=%s, smarks=%s, spno=%s where sid=%s",(sname,sbranch,smarks,spno,sid))
    mydb.commit()
    cursor.close()
    return redirect('/view')


if __name__=='__main__':
    app.run(debug=True)