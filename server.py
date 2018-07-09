from flask import Flask, render_template, request, redirect
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're usingcopy
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('lead_gen_business')
# now, we may invoke the query_db method

@app.route('/')
def index():
    query = mysql.query_db("SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(*) as count FROM leads JOIN sites ON leads.site_id = sites.site_id JOIN clients ON sites.client_id = clients.client_id GROUP BY client_name ORDER BY count")
    # print("Fetched all the stuff", query, "\n")
    return render_template('index.html', query = query)

if __name__ == "__main__":
    app.run(debug=True)