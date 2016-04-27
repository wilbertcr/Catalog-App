# Full Stack Web Developer Nanodegree

Project: Catalog App
============================================

Project Description:
============================================
* A one page web application displaying categories and the items of the currently selected category. 
User can add,edit and delete categories and add,edit and delete their respective items.
* Backend uses flask/SQLAlchemy/PostgreSQL
* Front uses React.js and JQuery for transmission of data.
* The backend of this application is strongly based on the restaurant menu app project in this nano-degree.
* The application uses tokens to prevent CSRF attacks and OAuth 2.0 via Google.

# First Run

**Prerequisites** 
You will need vagrant installed on your computer for this application to run.

First clone the repo and get inside the folder.

`$ git clone https://github.com/wilbertcr/Catalog-App.git`
`$ cd Catalog-App`

Run the virtual machine:

`$ vagrant up`

This may take a moment, since it has to provision the VM. Once that is finished, you will find an ssh key here:

`Catalog-App./vagrant/machines/default/virtualbox`

Use it to ssh into the box(I used putty). When you login you should see:

```
...
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 3.13.0-76-generic i686)

 * Documentation:  https://help.ubuntu.com/

  System information as of Wed Mar 16 18:10:15 UTC 2016

  System load:  0.9               Processes:           78
  Usage of /:   3.2% of 39.34GB   Users logged in:     0
  Memory usage: 15%               IP address for eth0: 10.0.2.15
  Swap usage:   0%

  Graph this data and manage this system at:
    https://landscape.canonical.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


The shared directory is located at /vagrant
To access your shared files: cd /vagrant
```

Go to the app folder:

`$ cd /vagrant/catalog/app`
 
And setup the database:

`$ ./setup_database.sh`

Get out:
`$ cd ..`

Run the application

`$ python run_app.py`

You should see something like this:

```
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```

At this point, the application is running. You can:

* Go to the web application:

 `http://localhost:5000`

* Access the atom feed:

`http://localhost:5000/items_feed`

* Get a json representation of all the categories and their respective items:
 `http://localhost:5000/categories/json`
 
* Get a json representation of a category by providing its id:
 `http://localhost:5000/category/<int:category_id>/json`

* Get a json representation of an item:

 `http://localhost:5000/item/<int:item_id>/json`

All of the above are accessible without logging in to the application.

To kill the app: CTRL-C

# Running the app after building.

Once the app has been built, you can restart it like this:

`$ python run_app.py`

# Documentation

```
├── catalog
    ├── run_app.py
    ├── app
        ├── build_React_app.sh
        ├── controllers.py
        ├── install_ReactJS_dev_packages.sh
        ├── package.json
        ├── setup_database.sh
        ├── components/
        ├── config/
            ├── config.py # Configuration file
        ├── db/
        ├── react_docs/
        ├── static/
        ├── templates/
        ├── tools/
```
*Created with esdoc

The backend's documentation(created using flask-autodoc), can be accessed by navigating to: 

*http://0.0.0.0:5000/documentation


# Building ReactJS App

In order for changes to the code to take effect you need to build the app.I used gulp to manage the building process. 

`$ cd catalog/app/tools`

**Build: Transpile, Package and Document**

`$ gulp`

**Watch catalog/app/components. Transpile and Package if files change.**

`$ gulp watch`

**Watch catalog/app/components. Build Documentation if files change.**

`$ gulp watch_documents`

**Build Documentation**

`$ gulp doc`

**Transpile Files**

`$ gulp transpile`

**Transpile and Package**

`$ gulp webpack`