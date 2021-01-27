# person_api
This project is created as test exercise for ТОО Biometric

## Installation

Copy this project on your local machine 
```
git clone https://github.com/outeqa1/person_api/
```
Install libraries
```
pip install -r requirements.txt
```
## Run app
```
python main.py
```
## Routes
```
/api/v1/people/
```
#### GET 
Returns all people
#### POST 
Creates person.
Example: /api/v1/people/ {"iin": "760724300757"}

```
/api/v1/people/<iin>
```
#### GET 
Returns person by iin.
Example: /api/v1/people/760724300757
