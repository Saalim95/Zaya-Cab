# Zaya-Cab
RESTful API for Cab Booking System

### Instructions:
1. Create the virtual environment by hitting following command in the Terminal ```virtualenv env```
2. Activate the virtual environment - ```env\scripts\activate```
3. Install all the depedencies given in the requirements.txt file - ```pip install -r requirements.txt```
4. Once all the depedencies get successfully installed in your virtualenvironment, then run the local server - ```python manage.py runserver```


### Tools required:

1. Python 3
2. Sqlite 3 (default)

### Virtual Env Libraries

1. Django==2.0.7
2. djangorestframework==3.8.2

### URLs for API methods

1. To register new commuter in the database - `localhost:<port number>/zayacab/user/register` and pass username and password in POST request parameters

2. To register new driver in the database - `localhost:<port number>/zayacab/driver/register` and pass username and password in POST request parameters

3. To get user trip history - `localhost:<port number>/zayacab/<commuter_id>/history`

4. To get user trip history - `localhost:<port number>/zayacab/<driver_id>/history`

5. To get the user location - `localhost:<port number>/zayacab/user/location/<commuter_id>`

6. To change the status of driver after booking and completion of a trip - `localhost:<port number>/zayacab/update/<driver_id>` and pass status params in POST request

7. To book a cab - `localhost:<port number>/zayacab/<commuter_id>/<driver_id>` and pass source, destination and fare in `POST` request.

8. Get the list of available drivers- # Zaya-Cab
RESTful API for Cab Booking System

### Instructions:
1. Create the virtual environment by hitting following command in the Terminal ```virtualenv env```
2. Activate the virtual environment - ```env\scripts\activate```
3. Install all the depedencies given in the requirements.txt file - ```pip install -r requirements.txt```
4. Once all the depedencies get successfully installed in your virtualenvironment, then run the local server - ```python manage.py runserver```


### Tools required:

1. Python 3
2. Sqlite 3 (default)

### Virtual Env Libraries

1. Django==2.0.7
2. djangorestframework==3.8.2

### URLs for API methods

1. To register new commuter in the database - `localhost:<port number>/zayacab/user/register` pass username and password in POST request parameters

2. To register new driver in the database - `localhost:<port number>/zayacab/driver/register` pass username and password in POST request parameters

3. To get user trip history - `localhost:<port number>/zayacab/<commuter_id>/history`

4. To get user trip history - `localhost:<port number>/zayacab/<driver_id>/history`

5. To get the user location - `localhost:<port number>/zayacab/user/location/<commuter_id>`

6. To change the status of driver after booking and completion of a trip - `localhost:<port number>/zayacab/update/<driver_id> and pass status params in POST request

7. To book a cab - `localhost:<port number>/zayacab/driver/available`
