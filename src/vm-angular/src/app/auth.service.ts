import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
// import { HttpService } from './http.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpClient) { }
  // constructor(private httpClient: HttpService) { }
  
  // sends user credentials and recieves an authorization token
  getToken(data){
	  return this.httpClient.post(`${this.API_URL}/auth/token`,data,{ observe: 'response' });
  }
}
