# Data Representation - Big Project
Prepared by: Sheldon D'Souza (G00387857)

## Project Objective:

The objective of the project is to program that demonstrates that you understand creating and consuming RESTful APIs

## Project Outline

The project has creates a flask server perform CRUD operations on a stocks and shares portfolio database. The database displays the stocks within a users portfolio. The user can add, delete and update the stocks in their portfolio 

## Contents of the repository

The contents of this repository are as follows:

1. .gitignore
2. LICENCE
3. Readme.md (this file)
4. dbconfigtemplate.py - This is the template file to add the local users database settings 
5. highlowDAO.py - The python file that gets the highs and lows from the external database and updates the high/low database
6. initdb1.sql - The configuration file to create the first database and tables
7. initdb2.sql - The configuration file to create the second database and tables
8. requirements.txt - The requirements file for running the program
9. server.py - The python file for the Flask server
10. StockDao.py - The python file that displays the top stocks and share from an external API and updates the stock_close table
11. apiLoad.html (staticpages folder) - Static webpage for to load the external API stocks
12. highLow.html (staticpages folder) -  Static webpage for to load the highs and lows from an external API of a stock based on user input
13. index.html (staticpages folder) - Static page which loads the stocks in the first database
14. login.html (staticpages folder) - Login page
15. loadHighLows.html (staticpages folder) - Static page which loads the highs and lows in the second database 
16. cream_dust.png (staticpages/img folder) - background image of the static pages 


## Layout of the websitse
1. The website starts on a login page where the user has to enter a username and password to proceed. The username is: G00387857@gmit.ie and the password is: password. Once the correct credentials have been entered it starts a session which will continue until the Logout button has been pressed.
2. The website will load the index page which will load the stocks and shares from the database. The database has the following fields:
	- ID - the ID entry in the database
	- Symbol - the symbol of the stock
	- Opening - The latest opening value of the stock
	- Closing - The latest closing value of the stock
	- Volume - The volume of stock traded on that day
This page  allows the user to:
	- create a stock record
	- update a stock record
	- delete a stock record
	- load a webpage with the top stocks via an external API
	- load a webpage which search for the highs and lows of a particular stock via an external API
3. The create record button will open up a page for the user to input the details of stocks (with the fields described on the index page) and add this stock to the database. It will also allow the user to return without adding
4. The load stock from API webpage will get the top stock from an external API. The API used is [MarketStack](https://marketstack.com/documentation). The user will need to enter an API key which this webpage will prompt the user to enter this key. <b>This key will be share with the reviewer of this project via email</b>. Once the Key is entered the top 10 stocks will be loaded with the fields mentioned on the index page. This webpage has the option to add the stock from the API to the local database
5. The Search for highs and lows webpage takes user input in the form of a stock symbol. When the user inputs a valid symbol, the website will once again ask for the external API key. Once this is entered the ID, Symbol, Highest price traded and the lowest price traded on the day are displayed. Note that all stock information is the last trading day available. Once the data is displayed there is a button to add the information to the database. Both the APIs have a temporary ID until they are input into the local database when they are auto allocated an ID. Also note that the highs and lows are a separate database from the user portfolio database.
6. The load highs and lows webpage will load and display the highs and lows that have been added to the database from step 5 above. The fields displayed will be the ones mentioned in step 5 above. There is also a button to delete and entry from a database and a button to return to the index page.
7. The logout button on each screen ends the session and brings the user back to the login page. 


## Running the program

To run the file do the following:

1. Install python (Anaconda) and SQL (mysql or equivalent)
2. Install the environment requirements from the requirements.txt
3. run the the .sql files to create the necessary databases (if they do not already exist) and create the tables based on the specific schema in these files
4. create the db1config.py and db2config.py files which will hold the sql user information and password as well as the databases from step 1 above
5. open a command terminal and navigate to the folder of the website
6. run the code ```python server.py```
7. once the server is running go to a webpage and enter http://127.0.0.1:5000/
8. navigate the website as mentioned in the Layout section of this readme
9. Use the API Key provided by email. Email me at G00387857@gmit.ie for the API key if you do not have it. 

## Key Features of the Website

1. The website runs a Python Flask server
2. The website has a login page which validates the session and keeps the user logged in until the logout button is used
3. The website connects to two databases. One for the user to view and add to the stock portfolio i.e. `stock_close` table within the `datarepresentation` database and the other to track an add the highs and lows of the stock i.e. `high_lows` table within the `highlow` database.
4. The website connect to an external API to obtain live information on stocks and shares
5. The websites uses styles, background images etc. to make it look nice.

## Next Steps

Next steps will be to attempt to host the website on an external server. 

## Contact
Email me at: [Sheldon D'Souza](G00387857@gmit.ie)