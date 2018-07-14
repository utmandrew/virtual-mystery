import { Injectable } from '@angular/core';
import { HttpService } from './http.service';

@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all of the auth component functions */
export class AuthService {
  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }
  
  // sends user credentials and recieves an authorization token (login)
  getToken(data){
	  return this.httpClient.post(`${this.API_URL}/auth/token`,data);
  }
}
