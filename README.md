## Project Title 
Analyzing Sports insights on Twitter, Reddit and Youtube

## Project Abstract

Sites like Twitter, Reddit and Youtube have given people a platform to engage with a single piece of content in many different ways. For developers, this presents an opportunity to measure different metrics on different platforms, and derive insights from the vast amount of data being generated. 
We have two major sporting events comingup: FIFA World cup Qatar 2022 and ICC Men’s T20 Worldcup. In this project, we use three major social media platforms: Twitter, Reddit and Youtube to analyze the popularity of these events indifferent parts of the world, the athletes and how the public engages with them and lastly, abusive content generated through thecourse of the events.

## Team - Data Doggers

* Pradnya Bhukan, pbhukan1@binghamton.edu
* Chelsea Olivia Fernandes, cferna10@binghamton.edu
* Sakshi Mendiratta, smendir1@binghamton.edu
* Tejal RahulDaga, tdaga1@binghamton.edu
* Jwalant Vishvesh Bhatt, jbhatt2@binghamton.edu


## Tech-stack

* `python` - The project is developed and tested using python v3.8. [Python Website](https://www.python.org/)
* `request` - Request is a popular HTTP networking module(aka library) for python programming language. [Request Website](https://docs.python-requests.org/en/latest/#)
* `flask` - Flask is a lightweight WSGI web application framework used for developing web applications . [Flask Website](https://flask.palletsprojects.com/en/2.2.x/)

## How to run the project?

Install `Python` and `Flask`

pip install flask
pip install requests
pip install nltk
pip install pandas
nltk.download('vader_lexicon')
pip install textblob
$ pip install -U textblob
$ python -m textblob.download_corpora

1. $ mkdir project_name
   $ cd project _name
   $ python3 -m venv venv
   $ . venv/bin/activate
   $ pip install Flask
2. Next run app.py file, this will generate a url
3. Navigate to :http://127.0.0.1:5000/home
