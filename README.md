# Project Name


<h3 align="center">
  :fireworks: Live demo :fireworks:
</h3>

<p align="center">
  > Live demo [_here_](https://www.books-api-bsski.herokuapp.com).
</p>


<div markdown="1" align="center">

old badges:
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/BSski/books-api/blob/main/LICENSE)

done badges:
[![Build Status](https://bsski.semaphoreci.com/badges/books-api/branches/main.svg?style=shields&key=bbf61a13-a31b-4766-99d2-8a8817119f9a)](https://bsski.semaphoreci.com/projects/books-api)
[![Demo Uptime](https://img.shields.io/uptimerobot/ratio/7/m791716455-288255922d4aaa0af095c195)](https://books-api-bsski.herokuapp.com/)


</div>

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Room for Improvement](#room-for-improvement)
* [Contact](#contact)
* [Author](#author)
<!-- * [License](#license) -->


## General Information
This is a project that was an old recruitment task of mine. I fixed points mentioned in the feedback and added dockerization and a CI/CD pipeline.
The project is a books API. It provides a feature to upload books from Google Books API to the database, and browse them, either with filters or without them.


## 🛠️ Technologies Used
- Django 4.0.3
- Django REST Framework 3.13.1 
- PostgreSQL
- Gunicorn 20.1.0
- Docker
- SemaphoreCI
- Heroku
- Coverage


## 🚀 Features
The recruitment task demanded such features and all are provided in a required format:
- accessing /books displays all stored books,
- accessing /books?published_date=1995 displays stored books published in a certain year,
- accessing /books?sort=-published_date displays all stored books sorted by published date in descending order,
- accessing /books?author=author1&author=author2 displays all stored books written by author1 and all stored books written by author2,
- accessing /books/<book_id> displays details of a single book of id <book_id>,
- sending a POST request to /db with a "q" keyword adds 10 books to the API's database; the books come from a query sent to the Google Books API with the passed keyword.

Furthermore, the API is deployed on Heroku from a Docker image using a CI/CD SemaphoreCI pipeline.

<screen of the CI/CD>


## :arrow_up: Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- Improvement to be done 1
- Improvement to be done 2

To do:
- Feature to be added 1
- Feature to be added 2


## Contact
Created by [@flynerdpl](https://www.flynerd.pl/) - feel free to contact me!


## ICON HERE Contact
-------------
- <contact.bsski@gmail.com>


:construction_worker: Author
-------------
- [@BSski](https://www.github.com/BSski)


## License
MIT
