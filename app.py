from flask import Flask,request,render_template, jsonify
app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_ops():
    if(request.method=='POST'):
        ops=request.form['operation']
        n1=int(request.form['num1'])
        n2=int(request.form['num2'])
        if ops=='Add':
            r=n1+n2
            result='The sum of '+str(n1)+' and '+str(n2)+' is '+str(r)
        elif ops=='Subtract':
            r=n1-n2
            result='The difference of '+str(n1)+' and '+str(n2)+' is '+str(r)
        elif ops=='Multiply':
            r=n1*n2
            result='The product of '+str(n1)+' and '+str(n2)+' is '+str(r)
        elif ops=='Divide':
            r=n1/n2
            result='The quotent of '+str(n1)+' and '+str(n2)+' is '+str(r)
        
        return render_template('results.html', result=result)
    
if __name__=='__main__':
    app.run(host='0.0.0.0')