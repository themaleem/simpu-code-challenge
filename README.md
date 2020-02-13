# Simpu code-challenge
My solution to the interview coding assesmen on [Kola-Simpu](https://github.com/kola-simpu/Coding-Challenge) github repo

steps to run the django project contained in this repo

 1. clone repo (or download manually) and navigate to folder directory on any CLI
 2. on the CLI, run  `pip install -r requirements.txt` to install project dependencies into current working environment
 3. user must have a MySQL interfacer installed on OS (i used xampp)
 4. create a MySQL database, and adjust the *DATABASE* settings located in the [core/settings.py](https://github.com/themaleem/simpu-code-challenge/blob/master/core/settings.py) file to fit the just created database name and host.
 5. on the CLI, run migrations , with command `python manage.py makemigrations`  followed by `python manage.py migrate`
 6. authentication purposes`python manage.py createsuperuser`
 7. run `python manage.py runserver`
 8. make a post request with your superuser credentials `http post :8000/api/token/ username=YOUR USERNAME password= YOUR PASSWORD`
 9. study cc/urls.py for other app url nagivations

