from flask import Flask , render_template,request
app = Flask(__name__)
user_data = {}
@app.route('/',methods=['GET', 'POST'])

def User_session():
    if request.method == 'POST':
     user_identifier = request.remote_addr
     user_inp  = request.form.get('user_input')
     user_data[user_identifier] = user_inp
    user_identifier = request.remote_addr
    user_input = user_data.get(user_identifier, '')

    return render_template('user_session.html', user_input=user_input)
if __name__ == '__main__':
   app.run(host='0.0.0.0',port=5001)

