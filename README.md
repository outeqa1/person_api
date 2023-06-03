# person_api

This project is created as test exercise for ТОО Biometric<br>
Description:
This app can calculate the appropriate age by IIN and save data in JSON format.

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

#### Create person.

Example (with POST method):

```
/api/v1/people/951010741253
```

#### Returns all peoples with valid IIN (with GET method):

```
/api/v1/people/
```

#### Returns only one person by iin (with GET method):

```
/api/v1/people/<iin>
```
