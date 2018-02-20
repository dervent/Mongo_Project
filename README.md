# MongoDB Project
This is the repository for group 5's Contemporary Databases (ISTE.438.01) project. 

# Initial Local Setup
**Setup steps:**
1. Clone the repository `Mongo_Project` and navigate to its local directory.
2. Ensure you have [Node.js](https://nodejs.org/en/) downloaded and installed.
3. Download Express web framework: <br/>
	`$ npm install express`
4. Download MongoDB driver for Node.js: <br/>
	`$ npm install mongodb`

**Running the app:**
 1. Copy the MongoDB files from `data\db` into your local directory that was set in your --dbpath <br/>
	 *E.g. On Windows, this directory is probably located in* `C:\data\db`
 2. Start your MongoDB server
 3. Go back to your local `Mongo_Project` directory and run: <br/>
	 `$ node app.js` <br/>
	 You should see `listening on port:3000` appear in your console.
 5. Go to your browser and type in `localhost:3000`. The application should now be in your browser window.
