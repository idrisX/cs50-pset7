from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir

from helpers import *

# configure application
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd
#which stocks the user owns


# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")#decorator
@login_required#decorator
def index():
    db.execute("SELECT* FROM transactions WHERE price_per_share=:price", price=lookup(stock_name)["price"]
    rows=db.execute("SELECT* FROM transactions")
    render_template("index.html", transactions=rows)
    #the numbers of shares owned
    # the current price of each stock
    #the total value of each holding
    return apology("TODO")



@app.route("/buy", methods=["GET", "POST"])#
@login_required
def buy():
    """Buy shares of stock.""" #create buy function
    purchase=db.execute("SELECT* FROM transactions WHERE price_per_share=:price"), price=lookup(stock_name).get("price")
    money=db.execute("SELECT* funds FROM users")
    if not money>=purchase:
        return apology("Not enough money")
    if money>=purchase:
        add=request.form.get("buy") 
        lookup(stock_name)
        db.execute("SELECT* FROM transactions WHERE price_per_share=:price", price=lookup(stock_name).get("price")
        db.execute("UPDATE transactions SET number_of_shares=:number_of_shares WHERE stock_name=:stock_name",number_of_shares=number_of_shares+add, stock_name=request.form.get("Stock Name"))
    #check to see if current money is greater than stock purchase
    #create new table
    #use index if you're gonna be searching through it a lot
    #use unique index if you just want to update row
    #update database
        return render_template("index.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    rows=db.execute("SELECT* FROM transactions")
    render_template("history.html", transactions=rows)
    #should simply be using data from tables
 



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear() #session is dictionary with all users

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # redirect user to home page
        return redirect(url_for("index"))#sends you to another index

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out."""
    stock_name=request.form.get("stock")
    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))



@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    stock_name=request.form.get("stock")
    lookup(stock_name)
    return render_template("quoted.html")
    




@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
    if request.method=="POST":
        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
            
            # ensure password was submitted
        elif not request.form.get("confirm_password"):
            return apology("must provide confirm_password")
        if request.form.get("password")!=request.form.get("confirm_password"):
            return apology("Passwords don't match")
        password=request.form.get("password")
        #hash password
        encrypted_password =pwd_contacts.encrypt(password)
        user_id=db.execute("INSERT INTO users(username, hash) VALUES(Username, Password)"),Username=request.form.get("username"),Password=request.form.get("password")
        session[]
        return redirect_url
    else:
        return render_template("register.html")
         
       
@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
   
    sell=db.execute("SELECT* FROM transactions WHERE number_of_shares=:shares", shares=request.form.get("number of shares")
    money=db.execute("SELECT* funds FROM users")
    # determine whether user has enough shares to sell
    if not sell<=held_shares:
        return apology("You don't have enough stocks")
    if sell<=heldshares:
        subtract=lookup(stock_name).get("price")
        held_shares=db.execute("SELECT* portfolio FROM transactions")
        db.execute("UPDATE transactions SET number_of_shares=:number_of_shares WHERE stock_name=:stock_name",stock_namenumber_of_shares=number_of_shares-subtract, stock_name=request.form.get("Stock Name"))
    
    
        return render_template("index.html")
    
@app.route("/change_password", methods=["GET", "POST"])
def change_password():
     newpassword=request.form.get("password")
     encrypted_new_password=pwd_contacts.encrypt(newpassword)
     db.execute("UPDATE users SET hash=:newhash ",encrypted_new_password)
     