import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpClient) { }
  
  // sends user credentials and recieves an authorization token
  getToken(data){
	  return this.httpClient.post(`${this.API_URL}/auth/token`,data);
  }
}
