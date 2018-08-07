import { Injectable } from '@angular/core';
import { HttpService } from '../http.service';

@Injectable({
  providedIn: 'root'
})
export class MysteryService {
  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }
  
  listRelease() {
	  // sends a request and recieves a list of releases
	  return this.httpClient.get(`${this.API_URL}/mystery/release/list`);
  }
  
}
