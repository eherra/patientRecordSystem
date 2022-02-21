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
- by setting 15 minutes session expiration time (considering [this](https://auth0.com/blog/balance-user-experience-and-security-to-retain-customers/#:~:text=How%20long%20should,for%20most%20businesses.))
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

#### User_info table

The table having more dynamic approach for storing the user info data:\
<code>key</code> column stores a key for a lookup of the specific user info (column <code>value</code>) which is wanted to be fetched. Keys used on the application: <code>name</code>, <code>phone</code>, <code>email</code>, <code>address</code> etc.

Due to the approach no need to determine what information is allowed to be stored on the database of the users if e.g. on further development is decided that more varies information is wanted to be stored. Also amount of columns on <code>users</code> table doesn't grow too large and can be kept clean and only for authorization usage.

**Example**

| id  | user_id | key | value |
| ------------- | ------------- | ------------- | ------------- |
| 1  | 1  | name  | Dan Dataman  |
| 2  | 1  | email  | dan@data.com  |
| 3  | 1  | phone  | +3519324123123  |
...

To fetch *name* (Dan Dataman) of the user can be done with SQL query:

```sql
SELECT value 
FROM   user_info 
WHERE  user_id = 1
AND    key = 'name'
```

Cons:\
Requires a bit more complex method for [initializing](https://github.com/eherra/patientRecordSystem/blob/master/repositories/users_repository.py#L98) user info when registering new user to the application.

### Known browser issues
All the functions are working on Google Chrome browser.

On *Mozilla Firefox* and *Safari* the appointment booking calender not working properly -> booking appointment for patient not possible while using these browsers.

Session timer not working on Safari.
