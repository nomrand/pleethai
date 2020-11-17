# Setup Development Environment
## 1. Install required software

Install software bellow (For the detailed operations to install, check the website of each software)
* Python
    * Version 3.6.7 recommended
    * Creating virtual environment recommended
    * The path to the Python executable must be set by the environment variable
* Git


## 2. Clone this project

```
git clone https://github.com/jocv-thai/pleethai.git
````


## 3. Install required Python packages

```
cd pleethai
pip install -r requirements.txt
````


## 4. Create database
````
python manage.py migrate
````


## 5. Create super user
````
python manage.py createsuperuser
````
* According to the displayed messages, enter username and password.


## 6. Start system
````
python manage.py runserver
````
* When you access `http://127.0.0.1:8000/` from a browser, you will see the "Search Page".


## 7. Register database
To register database, follow the steps in [How to add or edit words/sentences](./maintenance_dataedit.md).

* Refer to [Database](./database.md) for the details of each data to be registered
* [Sample data](https://drive.google.com/open?id=1AuRX2f7LATfLzXgWiI3-wmAbNUo3tt8o)
