from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    
    return render_template("index.html", mars_data=mars_data)



# Route that will trigger the scrape function
@app.route("/scrape")
def scraper():

    mars_datainfo = mongo.db.mars_data
    mars_data = scrape_mars.scrape_news()
    mars_data = scrape_mars.scrape_featureimg()
    mars_data = scrape_mars.scrape_facts()
    mars_data = scrape_mars.scrape_hemisphere()
    
    mars_datainfo.update({}, mars_data, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
