from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def books():           
        df = pd.read_csv('books.csv')
        data=request.get_json()
        user=data['user']
        bookid=df[df.name==user].bookid.values[0]
        bookdf=pd.read_csv('abc.csv')
        book=bookdf[bookdf.bookid==bookid]
        return {'book':book.to_dict()},200
    

@app.route('/api/users', methods=['GET','POST','DELETE'])
def users():
    df = pd.read_csv('users.csv')
    if request.method=='GET':
        df1 = df.to_dict()
        print(df1)
        return {'users':df1},200

    if request.method=='POST':
        data=request.get_json()
        user=[data['userid'],data['name'],data['bookid']]
        df=df.append(pd.Series(user,index=df.columns),ignore_index=True)
        df.to_csv('abc.csv',index=False)
        return {'message':'new user added'},201

    if request.method=='DELETE':
        data=request.get_json()
        df=df[df.name!=data['name']]
        df.to_csv('abc.csv',index=False)
        return {'message':'user deleted!!!!'},200



if __name__ == '__main__':
    app.run(debug=True)