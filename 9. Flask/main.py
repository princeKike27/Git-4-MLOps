# import modules
from flask import Flask, request, render_template

# instance of Flask
app = Flask(__name__) # __name__ specifies where Flask should look for files


# Home Page
@app.route('/')
def hello_world():
    return '<h1>Welcome to Flask App !!!</h1>'

# Players Page
@app.route('/players/<team>')
def players_page(team):
    return f'<h3>{team} Players Page</h3>'


# Square Page
@app.route('/square', methods=['GET'])
def square_number():
    # when user requests first time it will be None
    if(request.args.get('num') == None):
        return render_template('square.html')
    # if input i invalid
    elif(request.args.get('num') == ''):
            return "<html><body> <h1>Invalid input</h1></body></html>"
    else:
        number = request.args.get('num')
        square = int(number) * int(number)
        return render_template('solution.html', squareofnum=square, num=number)



# run 
if __name__ == '__main__':
    app.run()