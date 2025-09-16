from flask import Flask,render_template,request,redirect,url_for,jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def f1():
    return render_template('gpage.html')

@app.route("/mypage")
def f2():
    pname = 'pA'
    pid = 101
    pcost = 1000
    return render_template('products.html',tpname=pname,tpid=pid,tpcost=pcost)
@app.route("/mydata")
def f3():
    product_details = {}
    product_details['pid']=[101,102,103,104,105]
    product_details['pname']=['pA','pB','pC','pD','pE']
    product_details['pcost']=[1000,2000,3000,1200,3100]
    return jsonify(product_details)

@app.route("/mydb")
def f4():
    pid = 101
    pname = 'pA'
    pcost = 1230
    conn = sqlite3.connect('products.db')
    sth = conn.cursor()
    sth.execute("insert into product(pid,pname,pcost) values(?,?,?)",(pid,pname,pcost))
    sth.execute("insert into product(pid,pname,pcost) values(102,'pB',1255)")
    sth.execute("insert into product(pid,pname,pcost) values(103,'pC',2355)")
    sth.execute("insert into product(pid,pname,pcost) values(104,'pD',5555)")
    conn.commit()
    conn.close()
    return f"<h2><font color=green> Product details are inserted successfully</font></h2>"

@app.route("/dataview")
def f5():
    conn = sqlite3.connect('products.db')
    sth = conn.cursor()
    sth.execute('select *from product')
    records = sth.fetchall()
    products = {}
    products['K1'] = records
    return jsonify(products) # resonse - data response 
    

@app.route("/pageview")
def f6():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    sth = conn.cursor()
    sth.execute('select *from product')
    records = sth.fetchall()
    return render_template('pageview.html',trecords=records) # respons - webpage response 
    
    
if __name__ == '__main__':
    app.run(debug=True)