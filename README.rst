Squares Website Readme
======================

Purpose
--------

* This website was designed in Django to take in an integer
value X, between 1 and 100, and return a set of 100 squares, 
where the Xth square is colored red, and all others are grey.

Running
________

* The project is located at:
https://github.com/katerina7479/squares_site.git

* The project requirements are listed in requirements.txt

* To start the demonstration server, in the terminal navigate
to the /squares folder, and type:
python manage.py runserver

* In the browser, go to: http://127.0.0.1:8000

Structure
_________

* squares/urls.py was modified to direct root to the function main
in question/views.py

* No models were used, since the calculation could be done in javascript,
and it was not necessary to store any information. Therefor, sqlite3 was left
in place for /admin/ functions, but not used for the app.

* question/models.py was deliberately left blank.

* question/views.py function main takes in a HttpRequest, checks for method.
If GET, the form template is loaded and rendered, using RequestContext
to protect against cross-site request forgeries. (data is populated into 
the template {% csrf_token %}).

If POST, the squares template is generated, inserting the my_int variable into
the javascript var X. 

* In question/templates, the templates form.html and square.html 
extend base.html. 
