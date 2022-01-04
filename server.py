# Data Represenation Big Project
# Created By: Sheldon D'Souza - G00387857

from flask import Flask, url_for, request, redirect, abort, jsonify, session
from StockDao import stockDao
from highlowDAO import highlowDao # import DAO for highlows method

app = Flask(__name__, static_url_path='', static_folder='staticpages')
app.secret_key = 'thisismyHidden$ecretK3y' #secret key for session authentication

#main index page
@app.route('/')
def index():
    if not 'username' in session: #added the authentication in each @app.route
        return redirect("login.html")
    else:
        return redirect("index.html")

#access check for API Load
@app.route('/apiLoad')
def apiLoad():
    if not 'username' in session:
        return redirect("login.html")
    else:
        return redirect("apiLoad.html")
        
#access check for high low
@app.route('/highLow')
def highLow():
    if not 'username' in session:
        return redirect("login.html")
    else:
        return redirect("highLow.html")



# Redirect from the login page will create a valid session (login has not been validated here)
@app.route('/loginsuccess')
def loginsuccess():
    session['username'] = "confirmed"
    return redirect("index.html")

# Logout button code
@app.route('/logout')
def logout():
    session.pop('username', None) #pop the username to be None and therefore end the session
    return redirect("login.html")


#Add from API
@app.route('/addFromAPI', methods=['POST'])
def addFromAPI():
        if not 'username' in session:
            return redirect("login.html")
        else:
            if not request.json:
                abort(400)

            #populate the stock dictionary based on the data recieved from ajax and add this to database via python method
            stock = {
                "symbol": request.json["symbol"],
                "open": request.json["open"],
                "close": request.json["close"],
                "volume": request.json["volume"]
            }
            #print(stock)
            return jsonify(stockDao.addfromAPI(stock))

#Highs and Lows
@app.route('/highLowFromAPI', methods=['POST'])
def highLowFromAPI():
        if not 'username' in session:
            return redirect("login.html")
        else:
            if not request.json:
                abort(400)

            #populate the stock dictionary based on the data recieved from ajax and add this to database via python method
            stock = {
                "symbol": request.json["symbol"],
                "high": request.json["high"],
                "low": request.json["low"]
            }
            print(stock)
            return jsonify(highlowDao.highLowsAPI(stock))


#get all - used to show all stocks and shares in the portfolio
@app.route('/stocks')
def getAll():
    if not 'username' in session:
        return redirect("login.html")
    else:
        return jsonify(stockDao.getAll())

#get all High Low - used to show all high lows in the portfolio
@app.route('/highs')
def getAllHigh():
    if not 'username' in session:
        return redirect("login.html")
    else:
        return jsonify(highlowDao.getAll())


#delete an entry from the HighLow database and html table
@app.route('/highs/<int:ID>', methods=['DELETE'])
def deleteHigh(ID):
    if not 'username' in session:
        return redirect("login.html")
    else:
        highlowDao.delete(ID)

        return jsonify({"done": True})



# find By id - used to find a particular stock by it's ID
@app.route('/stocks/<int:ID>')
def findById(ID):
    if not 'username' in session:
        return redirect("login.html")
    else:
        return jsonify(stockDao.findById(ID))


# create a new stock entry in the database
@app.route('/stocks', methods=['POST'])
def create():

    if not 'username' in session:
        return redirect("login.html")
    else:
        if not request.json:
            abort(400)

        stock = {
            "ID": request.json["ID"],
            "symbol": request.json["symbol"],
            "open": request.json["open"],
            "close": request.json["close"],
            "volume": request.json["volume"]
        }
        return jsonify(stockDao.create(stock))

#update a particular stock entry for given parameters
@app.route('/stocks/<int:ID>', methods=['PUT'])
def update(ID):
    if not 'username' in session:
        return redirect("login.html")
    else:
        foundStock=stockDao.findById(ID)
        print (foundStock)
        if foundStock == {}:
            return jsonify({}), 404
        currentStock = foundStock
        if 'symbol' in request.json:
            currentStock['symbol'] = request.json['symbol']
        if 'open' in request.json:
            currentStock['open'] = request.json['open']
        if 'close' in request.json:
            currentStock['close'] = request.json['close']
        if 'volume' in request.json:
            currentStock['volume'] = request.json['volume']
        stockDao.update(currentStock)

        return jsonify(currentStock)

#delete an entry from the database and html table
@app.route('/stocks/<int:ID>', methods=['DELETE'])
def delete(ID):
    if not 'username' in session:
        return redirect("login.html")
    else:
        stockDao.delete(ID)

        return jsonify({"done": True})



if __name__ == "__main__":
    app.run(debug=True)