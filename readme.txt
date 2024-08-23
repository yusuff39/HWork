ProgX
This program allows users to list, add, delete and update data in a JSON file. With a simple user interface, you can easily perform basic data management operations.,


required
Python + tkinter lab
mongodb (optional)

Steps
1. Install Python on your computer.

2. Run `pip install` in the terminal to install the necessary libraries:

	pip install tkinter

3. MongoDB Installation:

Download MongoDB:

The easiest way to download MongoDB is to download the Community Edition version from the official MongoDB website.
Select the version that suits your operating system and start the download.
Install MongoDB:

Windows:
Run the downloaded .msi file.
Follow the installation wizard and complete the installation using the default settings.
Check the "Install MongoDB as a Service" option so that MongoDB can run automatically in the background.

Verify MongoDB is Working:

Open the MongoDB command line (shell) by entering the mongo command in the terminal.
Enter a simple command to check if MongoDB is working properly:

Copy the code : show dbs
This command will list the available databases. If you do not receive any errors, MongoDB is working successfully.
Using MongoDB:

You can create databases, add collections, and work with data in the MongoDB command line.
Make sure the MongoDB server is open before running the project.

4. Run it final_json.py 

This program accesses the data in the json file named fake json and performs add, delete and update operations on them.

5. Run it final_mongo_db.py (optional)

This program reads the data in the fake json file. 
Mongodb on the computer opens a new area and writes the data there. Then it performs add, delete, update operations on the data.