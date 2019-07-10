from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<name>') 
def hello(name):
    print(name)
    return f"Hi {str(name)}! "

@app.route('/repeat/<num>/<name>') 
def repeat(num,name):
    print(name)
    return (str(name) * int(num)) 

# @app.route('/say/flask')
# def hi_flask():
#     return 'Hi Flask!'

# @app.route('/say/michael')
# def hi_michael():
#     return 'Hi Michael!'

# @app.route('/say/john')
# def hi_john():
#     return 'Hi John!'

# @app.route('/repeat/35/hello')
# def hello_35():
#     for i in range(1,36,1):
#         print 'hello'
#         return 'hello'
# hello_35()


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    
if __name__!="__main__":   # Ensure this file is being run directly and not from a different module    
    print("Heckie Naw Jo!!!")    # Run the app in debug mode.