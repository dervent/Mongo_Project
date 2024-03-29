# MongoDB Project
This is the repository for group 5's Contemporary Databases (ISTE.438.01) project. 

## Initial Local Setup
**Setup steps:**
1. Clone the repository `Mongo_Project` and navigate to its local directory.
2. Ensure you have [Python 2.7](https://www.python.org/downloads/) downloaded and installed. Ensure Python is part of `PATH`.
3. Download and install Pip: <br/>
   a. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) and save to a local directory <br/>
   b. Install Pip by running: `$ python get-pip.py` <br/>
   c. Verify successful installation by running with no errors: `$ pip freeze` <br/>
4. **(Optional)** Set up and work in a virtual environment. <br/>
    a. Install virtual environment & virtual environment wrapper <br/>
        `$ pip install virtualenv`<br/>
        `$ pip install virtualenvwrapper`<br/>
        `$ pip install virtualenvwrapper-win` _(for Windows only)_ <br/>
    b. Create and activate your virtual environment <br/>
        `$ mkvirtualenv mongo_project` _(or any name you would like)_ <br/>
        `$ workon mongo_project` <br/>
5. At the top level of your `Mongo_Project` directory, install all the Python dependencies you will need for the project. <br/>
	`$ pip install -r requirements.txt` <br/>
    _If there are any more dependencies/modules that you have to use, add them to the text file._

## Running the App Locally
 1. Ensure you have started up your local MongoDB database (and optionally, activated your virtual environment)
 2. Navigate to the `Mongo_Project\app` directory and set the `FLASK_APP` env variable <br/>
    `$ set FLASK_APP=app.py` _(use `export` on Mac)_
 3. Run the application <br/>
    `$ flask run` <br/>
 4. Open a browser and navigate to `http://127.0.0.1:5000/` to interact with the app

## References
- [Python & pip Windows installation](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation)