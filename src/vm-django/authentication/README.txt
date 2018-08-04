# Authentication Framework

## Usage

Notes:
 * All of these requests require an authentication token in the header
 - Uses django-rest-framework token authentication
 - Token does not expire at a given time interval
 - Token is reset for each user once the user logs out

** Definition **

Get a user's token and mystery hash on valid login.

Note: New auth token is created if one doesn't exist.

** Request **

`POST /auth/token`

JSON:

 [
     {
	"username": username,
	"password": password
     }
 ]

** Response **

 - 200 OK on success
 - 400 BAD REQUEST on failure

JSON:

 [
     {
	"token": authtoken,
	"mystery": mysteryhash
     }
 ]

** Definition **

Log user out by deleting auth token.

** Request **

`GET /auth/logout`

** Response **

 - 200 OK on success
 - 400 BAD REQUEST on failure