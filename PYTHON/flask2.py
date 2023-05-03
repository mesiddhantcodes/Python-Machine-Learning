from flask import Flask,render_template,redirect,jsonify,request
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home_page():
    return render_template('index.html')
#fsdfjhasdjklfghbdfasjsdfdf

@app.route('/math',methods=['POST'])
def math_operation():
    if(request.method =='POST'):
        obs=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        #The data which is come from the form 
        #above three data is come from the form
        if(obs=='add'):
            r = num1+num2
            result='this is the sum of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        if(obs=='subtract'):
            r = num1-num2
            result='this is the subtraction of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        if(obs=='multiply'):
            r = num1*num2
            result='this is the multiply of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        if(obs=='divide'):
            r = num1/num2
            result='this is the divide of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        
        
        return render_template('results.html',result=result)
    


@app.route('/post_man',methods=['POST'])
def math_operation1():
    if(request.method =='POST'):
        obs=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        #The data which is come from the form 
        #above three data is come from the form
        if(obs=='add'):
            r = num1+num2
            result='this is the sum of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        if(obs=='subtract'):
            r = num1-num2
            result='this is the subtraction of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        if(obs=='multiply'):
            r = num1*num2
            result='this is the multiply of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        if(obs=='divide'):
            r = num1/num2
            result='this is the divide of '+ str(num1)+ ' and '+ str(num2) + ' is ' + str(r)
        
        
        return jsonify(result)








if __name__=="__main__":
    app.run(host="0.0.0.0")
