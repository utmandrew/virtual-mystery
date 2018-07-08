import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor() { }
  
  private token: string = "";
  
  setToken(newToken: string) {
	  this.token = newToken;
  }
  
  getToken() {
	  return this.token;
  }
}
