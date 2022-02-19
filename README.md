## Patientlify - A Digital Patient Record System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

### About 

An application for hospitals in order to keep track of their patients appointments, prescriptions, symptom stories and enable patient <-> doctor communication.

The project's main focus has been on diverse SQL queries (CRUD) usage. 

As being healthcare related application and storing sensitive data of its users - I have been focusing on the security e.g.:
- by setting 15 minutes session expiration time (event though conflicting [this](https://auth0.com/blog/balance-user-experience-and-security-to-retain-customers/#:~:text=OWASP%20recommends%20application%20builders%20to%20implement%20short%20idle%20time%20outs%20(2%2D5%20minutes)%20for%20applications%20that%20handle%20high%2Drisk%20data%2C%20like%20financial%20information.%20It%20considers%20that%20longer%20idle%20time%20outs%20(15%2D30%20minutes)%20are%20acceptable%20for%20low%2Drisk%20applications.)) 
- admin (doctor) role check when calling POST-methods which usage is only authorizited by this role
- users don't have access to pages/information which are not their _own_ information

Input validations (client-side and e.g. via Postman) has been taking consideration and secured that users can't pass data through which is not formatted according to validations rules.

### Hosting

Application is hosted on:\
https://patientlify.herokuapp.com/

I have added 2 test users to Heroku Postgres DB in order to test the app:

#### Patient
- username: patient123
- password: testPassword

#### Doctor
- doctor123
- testPassword

You can also create your own user from:\
https://patientlify.herokuapp.com/register

### Functionalities of the application

**Admin (doctors) available to do:**
- [x] write symptom stories to their patients
    - [x] edit/delete symptom stories 
- [x] create new prescriptions
- [x] determine prescription for patients
    - [x] add prescriptions to patient
    - [x] delete prescriptions from patient
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
    - [x] upcoming/past appointments
- [x] see their doctor's information (contact - phone)
- [x] send message to their doctor
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

### Input validation
The app has client-side validations for user inputs done via HTML5 **required**, **min-, maxlength** and regex **pattern** matches.

On backend input validations has been done for cases where higher amount of form parameters is given with a validation model [classes](https://github.com/eherra/patientRecordSystem/tree/master/utils/validators/models) when registering new user and updating user settings. 
The validation class takes a form as a construct parameter and checks that the form values are according to the validation rules and raises value error if the rules are not met.

### DB diagram
![Db diagram](/database/diagram.png)

DB schema with constraints included can be found ->
[DB schema](https://github.com/eherra/patientRecordSystem/blob/master/database/schema.sql)

### Known browser issues
On *Mozilla Firefox* and *Safari* the appointment booking calender not working properly -> booking appointment for patient not possible while using these browsers.

### Backlog

#### Frontend

#### Backend

#### General
