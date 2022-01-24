## A Patient Record System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

Patient record system for hospitals in order to keep track of their patients appointments, prescriptions and symptoms stories. 

### TODO
- input validations
- proper error handeling
- refactoring
- heroku and config heroku db
- login and session addition
- features listed below

<b>Admin (doctors) available to do:</b>
- [x] write symptom stories of patients
    - [x] delete symptom stories 
    - [x] edit symptom stories 
- [ ] determine prescription for patients
    - [x] delete prescriptions from patient
    - [ ] add new prescriptions to prescriptions db table
- [ ] book appointments for a patient
- [ ] see their own list of patients
- [ ] send message to their patients
- [ ] read messages
- [x] edit profile details
    - [x] name
    - [x] email
    - [x] phonenumber
    - [x] address
        - [x] city
        - [x] country

<b>User (patients) available to do:</b>
- [ ] see their own records
    - [x] prescriptions
    - [ ] symptons stories
- [ ] see their doctor's information (contact - email/phone)
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