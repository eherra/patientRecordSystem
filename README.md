## Patientlify - A Patient Record System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

Patient record system for hospitals in order to keep track of their patients appointments, patient <-> doctor communication, prescriptions and symptom stories. 

### Hosting

Application is hosted on Heroku:

https://patientlify.herokuapp.com/

I have added 2 test users to Heroku Postgres DB in order to test the app:

#### Patient
- username: patient123
- password: testPassword

#### Doctor
- username: doctor123
- password: testPassword

You can also create your own user if you wish to.

### Known browser issues
On *Mozilla Firefox* and *Safari* the appointment booking calender not working properly -> booking appointment for patient not possible while using these browsers.

### Functionalities of the application

**Admin (doctors) available to do:**
- [x] write symptom stories to their patients
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
    - [x] sent history
    - [x] received history
- [x] edit profile details
    - [x] name
    - [x] email
    - [x] phonenumber
    - [x] address
        - [x] city
        - [x] country

**User (patients) available to do:**
- [x] see their own records
    - [x] prescriptions
    - [x] symptons stories
- [x] see their doctor's information (contact - phone)
- [x] send message to their doctor
- [x] read messages
    - [x] sent historys
    - [x] received history
- [x] edit profile details
    - [x] name
    - [x] email
    - [x] phonenumber
    - [x] address
        - [x] city
        - [x] country

### Input validation
The app has client-side validations for user inputs done via Bootstrap **required** and regex **pattern** matches.

On server-side the inputs are as well validated -> via Postman incorrect data can't be sent and inserted to the database.

The input validations has been done for cases where higher amount of form parameters is given with a validation model class e.g. when registering new user, and updating user settings. 
The validation class takes a form as a construct parameter and checks that the form values are according to validation rules.

### Backlog

#### Frontend
- error pages 404, 500
- message history arrow 180 degree turn when opened

#### Backend
- db table values (UNIQUE/NULL)

#### General
- refactoring
    - templates
    - CSS files?