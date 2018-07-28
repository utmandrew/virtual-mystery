# Comment and Reply Framework

## Usage

NOTE: All of these requests require an authentication token in the header.


** Definition **

Get a sorted list of comments and replies for a specific mystery release.

** Request **

`GET /comment/<release#>`

** Response **

 - 200 OK on Success
 - 400 BAD REQUEST on Failure
 - 403 FORBIDDEN if user has not yet commented

JSON:

 [
     {
	"id": commentid,
	"reply": [
 	   {
		"id": replyid,
		"text": replytext,
		"username": replyowner
	   }
	 ],
	"text": commenttext,
	"username": commentowner
     }
 ]



** Definiton **

Create a new comment for the users mystery and current release.

** Request **

`POST /comment/create`

JSON:

 [
     {
	"text": commenttext
     }
 ]

** Response **

 - 201 Created on Success
 - 400 BAD REQUEST on Failure
 - 403 FORBIDDEN if user has previously commented


** Definiton **

Create a new reply for a specific comment and return the newly created reply.

** Request **

`POST /comment/reply`

JSON:

 [
     {
	"parent": parentcommentid,
	"text": replytext
     }
 ]

** Response **

 - 201 Created on Success
 - 400 BAD REQUEST on Failure

JSON:

 [
     {
	"id": replyid,
	"text": replytext,
	"username": replyowner
     }
 ]
