#!C:\Users\ysj30\Anaconda3\python.exe

print ("Content-type: text/html")
print()

import mysql.connector

# import and enable CGI traceback - so errors will show in the browser
import cgitb
cgitb.enable()

database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "netflix-search"
)

print("""
<h1> Connected </h1>
""")