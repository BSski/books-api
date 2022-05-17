<p align="center">
  <h2 align="center">Django Books API</h2>
</p>


<div markdown="1" align="center">

[![Build Status](https://bsski.semaphoreci.com/badges/books-api/branches/main.svg?style=shields&key=bbf61a13-a31b-4766-99d2-8a8817119f9a)](https://bsski.semaphoreci.com/projects/books-api)
[![Demo Uptime](https://img.shields.io/uptimerobot/ratio/7/m791716455-288255922d4aaa0af095c195)](https://books-api-bsski.herokuapp.com/)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/BSski/books-api/blob/main/LICENSE)
[![Heroku](https://pyheroku-badge.herokuapp.com/?app=books-api-bsski&style=flat)](https://books-api-bsski.herokuapp.com/)
[![Maintainability](https://api.codeclimate.com/v1/badges/c69d9019a58cd920e18e/maintainability)](https://codeclimate.com/github/BSski/books-api/maintainability)
[![CodeFactor](https://www.codefactor.io/repository/github/bsski/books-api/badge)](https://www.codefactor.io/repository/github/bsski/books-api)
[![codecov](https://codecov.io/gh/BSski/books-api/branch/main/graph/badge.svg?token=1T80VR8JBB)](https://codecov.io/gh/BSski/books-api)

</div>


<h3 align="center">
  :fireworks: Live demo :fireworks:
</h3>

<p align="center">
  https://books-api-bsski.herokuapp.com/
</p>



## Table of contents
* [Project description](#scroll-project-description)
* [Technologies used](#hammer-technologies-used)
* [Features](#rocket-features)
* [Room for improvement](#arrow_up-room-for-improvement)
* [Contact](#telephone_receiver-contact)
* [Author](#construction_worker-author)
* [License](#unlock-license)


## :scroll: Project description
This is a project that was a previous recruitment task of mine. I fixed the points mentioned in the feedback and added dockerization, a CI/CD pipeline on SemaphoreCI, gunicorn, and changed hosting from pythonanywhere to heroku.
The project is a books API: it provides a feature to upload books from Google Books API to the database, and browse them (with optional filters).


## :hammer: Technologies used
- Python 3.9.12
- Django 4.0.3
- Django REST Framework 3.13.1 
- PostgreSQL 14.2
- Gunicorn 20.1.0
- Docker
- SemaphoreCI
- Heroku


## :rocket: Features
The recruitment task demanded such features and all are provided in a required format:
- accessing `/books` displays all stored books,
- accessing `/books?published_date=<year>` displays stored books published in a certain year,
- accessing `/books?sort=-published_date` displays all stored books sorted by published date in descending order,
- accessing `/books?author=<author1>&author=<author2>` displays all stored books written by _author1_ and all stored books written by _author2_,
- accessing `/books/<book_id>` displays details of a single book of id _book_id_,
- sending a POST request to `/db` with a `q` keyword adds 10 books to the API's database; the books come from a query sent to the Google Books API with the passed keyword and the operation will update existing books if there are such.

Furthermore, the API is deployed on Heroku from a Docker image using a CI/CD SemaphoreCI pipeline:

![CI/CD screenshot](https://i.imgur.com/0NfYohr.png)


## :arrow_up: Room for improvement

Room for improvement:
- sorting books with incomplete date as if they were written 1st of January, but displaying year only, instead of the current solution,
- more tests.

## :telephone_receiver: Contact
- <contact.bsski@gmail.com>


## :construction_worker: Author

- [@BSski](https://www.github.com/BSski)


## :unlock: License
MIT
