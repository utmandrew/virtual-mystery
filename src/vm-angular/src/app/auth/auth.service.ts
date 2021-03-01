import { Injectable } from '@angular/core';
import { HttpService } from '../http.service';

@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all of the auth component functions */
export class AuthService {
  API_URL = '/api';

  constructor(private httpClient: HttpService) { }

  // sends user credentials and recieves an authorization token (login)
  getToken(data) {
    return this.httpClient.post(`${this.API_URL}/auth/token`, data);
  }

  deleteToken() {
    // log user out
    return this.httpClient.get(`${this.API_URL}/auth/logout`);
  }

  // sends new password credentials and recieves confirmation
  changePassword(data) {
    return this.httpClient.post(`${this.API_URL}/auth/changepassword`, data);
  }

  // returns true iff user is logged in, otherwise returns false
  getUser() {
    return sessionStorage.getItem('currentUser') != null;
  }

  getUserType() {
    return JSON.parse(sessionStorage.getItem('currentUser')).is_ta;
  }

}
