[Return to ReadMe file](README.md)

## Table of Contents

### 1. [Version Control](#version-control)

### 2. [Heroku](#heroku)

### 3. [Amazon Web Services](#aws)

### 4. [Github](#github)


## Version Control

- This project was built using [GitPod](https://gitpod.io/workspaces/) as the code editor.

- The repository is hosted on [Github](https://github.com/) with all code being stored here.

- For the build of this project Git has been used for all version control. 

- A few occasions that I needed to go back to a previous commit, the command `git revert <COMMIT ID>` was used.


## Heroku

The crafty shop project is live and deployed to [Heroku](https://dashboard.heroku.com/). To deploy your own project using Python and Djano, follow the below steps:

1. All the project dependencies, packages, and requirements installed have to be included in a `requirements.txt` file, placed on the root directory. To automatically save all the installed dependencies you can use the command `pip3 freeze > requirements.txt`. If you haven't created a file before running this command, it will automatically create one for you. If at any point you need to install all the dependancies stated on the requirements file, you can do so by running the `pip3 install -r requirements.txt` command. 

2. Make sure you set then environment variables either on a `env.py` or on the gitpod variables, accessed from the workspace page, inside the settings tab.
Create a new SECRET KEY and make sure not to include any of the passwords on version control! 
- If you have already set your STRIPE account, you can find the necessary stripe keys within the API and Webhook tabs.
- Set these variables:
    ```
    SECRET_KEY = <'Your Key Here'>
    STRIPE_SECRET_KEY = <'Your Key Here'>
    STRIPE_PUBLIC_KEY = <'Your Key Here'>
    ```
3. Create a Procfile file. Without this, Heroku cannot successfully execute and run. This file lets Heroku know what server is being used. For this, install `Gunicorn`, and add the following line to your Profile document: `web: gunicorn [YOUR APP NAME].wsg:application `

4. Commit and Push all those changes to the GitHub repository.

5. Login to your Heorku account and select 'Create New App' at the top right. Choose a unique name and select a region closest to you.

    ![Screenshot of heroku create a new app option](docs/Readme/deployment/heroku-new-app.png)

6. Choose the provisions tab and select Postgres database for the app. Search Heroku Postgres and choose the 'Hobby Dev - Free' option.

7. If not done yet, using the command line install the following:
    - `pip3 install dj_database_url`
    - `pip3 install psycopg2-binary`
    - `pip2 install gunicorn`

8. On settings.py import dj_database_url at the top and remove the Django database configurationa and replace with:

    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    ```
    this will set the logic to use either the local or the heroku database on development or production.

9. Find `DATABASE_URL` variable to your Heroku variables (under settings). Click reveal config vars and copy the variable. Add it to your local environment and If using Gitpod, restart the workspace.

    ![Screenshot Heroku Config Vars](docs/Readme/deployment/heroku-reveal-config-vars.png)#

10. In your IDE, migrate the local database to Heroku. start with the with the models first:
    - Run `python3 manage.py migrate`
    - Then to re-create the database run - `python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json` this creates a backup of the database and dumps all necessary data into a json file.
    - To export this data to Heroku run - `python3 manage.py loaddata db.json`

11. To access the admin dashboard of the site, you have to create asuperuser for the deployed version:
    - `python3 manage.py createsuperuser` and fill the required fields

12. Before deployment, it's necessary to tell Heroku not to collect static files. Within the Heroku Vars add a new variable:
`DISABLE_COLLECTSTATIC = 1`

13. Add the new app name to the allowed hosts within settings.py: 
    - Example: `ALLOWED_HOSTS = ['crafty-shop.herokuapp.com', 'localhost']`

14. Once everthing is in place, you can add, commit and push the changes to the repository

15. Once again, you need to push the main branch to Heroku. Use these commands:
    - `heroku git:remote -a heroku-app-name`
    - `git push heroku main`

16. To allow automatic pushes to the main Heroku branch, You can connect automatic deployments connecting heroku to github. Once it's connected go to the bottom of the page and select 'Enable Automatic Deployments'.

    ![Screenshot connect heroku to github for automatic deployment](docs/Readme/deployment/heroku-connect-github.png)


