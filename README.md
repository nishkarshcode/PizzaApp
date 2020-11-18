# Pizza Application
This is only for the test Purpose

## Building

First create a virtual Environment in you system and install and the dependancy

```sh
$ python -m venv MyPizza
$ source venv/bin/activate
$ pip install -r requirements.txt
```
	
## Pip Modules Used
Python modules:
* djnago3.0
* djangorestframework3.12.2
* psycopg22.8.6
	
## Get involved!
clone the project from repository
* `git clone git@github.com:nishkarshcode/PizzaApp.git`

## Walkthrough
* You just need to create Toppings Firsts use POST call to add or GET call to sell all the toppings
  http://127.0.0.1:8000/pizza/toppings/
* To create a regular pizza and a square pizza, Use POST call of below link to create and GET for see all pizza
  http://127.0.0.1:8000/pizza/allpizza/
* To filter the pizza based on size, type. Simply add parameter to the below links
  http://127.0.0.1:8000/pizza/allpizza/?sizes=medium
* To delete any of the listed pizza. Add id to blelow link and use DELETE method
  http://127.0.0.1:8000/pizza/allpizza/2/


