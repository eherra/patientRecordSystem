## Patientlify - A Patient Record System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

Patient record system for hospitals in order to keep track of their patients appointments, prescriptions and symptom stories. 

### Hosting

Application is hosted on Heroku:

https://patientlify.herokuapp.com/

Registering new users functionality is in progess.

Therefore I have added 2 test users to Heroku Postgres DB in order to test the app:

#### Patient
- username: patient123
- password: testPassword

#### Doctor
- username: doctor123
- password: testPassword

### Functionalities of the application

<b>Admin (doctors) available to do:</b>
- [x] write symptom stories of patients
    - [x] delete symptom stories 
    - [x] edit symptom stories 
- [x] determine prescription for patients
    - [x] add prescriptions to patient
    - [x] delete prescriptions from patient
        - [x] add new prescriptions to prescriptions db table
- [x] book appointments for a patient
    - [x] delete appointments
- [x] see their own list of appointments
- [x] send message to their patients
- [x] read messages
- [x] edit profile details
    - [x] name
    - [x] email
    - [x] phonenumber
    - [x] address
        - [x] city
        - [x] country

<b>User (patients) available to do:</b>
- [x] see their own records
    - [x] prescriptions
    - [x] symptons stories
- [x] see their doctor's information (contact - phone)
- [x] send message to their doctor
- [x] read messages
    - [x] see sent historys
    - [x] see received history
- [x] edit profile details
    - [x] name
    - [x] email
    - [x] phonenumber
    - [x] address
        - [x] city
        - [x] country

### Backlog

#### Frontend
- js input validations
- action success/failure feedback
- error pages 404, 500
- message history arrow 180 degree turn when opened
- register user possible to register doctor or patient button
- appointment page
    - cleaner user info
    - cleaner appointmet details
    - top right part, photo?

#### Backend
- proper input validations
    - starting to use validator module and moving validator methods there
- proper error handeling
- patient not having access to admin routes (test via Postman)
- register new user functions
- db table values (UNIQUE/NULL)

#### General
- refactoring
    - folder structure
    - templates
    - usage of Blueprints?
    - addings tests