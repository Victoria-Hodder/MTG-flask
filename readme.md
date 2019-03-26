# Bootstrap 4 Flask BoilerPlate

## Core Files

[.gitignore](gitignore) - This specifies which files and directories that git can ignore in a project. You would normally put your virtualenv folder in here along with any .pyc files. 

[Procfile](Procfile) - This is specific Heroku and possbly other enviroments

[requirements.txt](requirements.txt) - This file is used to keep track of all the librariies that need to be installed. You will be developing/testing/deploying on different machines and the you will run the comman below after you have set up your virtual environment to install all the required libraries to run the project 

		pip install -r requirements.txt

[run.py](run.py) - This is a standard file, it doesn't change from project to project. It specifies the server setup

		python run.py

[runtime.txt](runtime.txt) - This is another file specific to Heroku deployment. It specifies which version of Python should be used for the project. 

[app/__init__.py](app/__init__.py) - This is where you initialize your app

[app/views.py](app/views.py) - This is where the bulk of your code will go for a basic app. It is where the routes are created and where you decided which template to render. 