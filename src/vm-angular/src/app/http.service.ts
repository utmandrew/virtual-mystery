import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
// import { Http, Headers } from '@angular/http'; *old code
import { UserService } from './user.service';

@Injectable({
  providedIn: 'root'
})

// Wraps the HttpClient object to add the current users authorization token
export class HttpService {

  constructor(private http: HttpClient, private user: UserService) { }
  
  // returns an HttpHeaders object with the current user's auth token
  addAuthToken(header: HttpHeaders){
	  return header.append('Authorization', 'Token ' + this.user.getToken());
  }
  
  // performs a get request after calling the addAuthToken function
  get(url) {
	  let header = new HttpHeaders();
	  header = this.addAuthToken(header);
	  return this.http.get(url, {headers: header});
  }
  
  // performs a post request after calling the addAuthToken function
  post(url, data) {
	  let header = new HttpHeaders();
	  header = this.addAuthToken(header);
	  return this.http.post(url, data, {headers: header});
  }
  
}
