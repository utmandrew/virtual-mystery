import { Injectable } from '@angular/core';
import { HttpService } from '../http.service';
import {HttpClientModule} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MysteryService {

  constructor(private httpClient: HttpService) { }

  listRelease() {
	  // sends a request and recieves a list of releases
	  return this.httpClient.get(`mystery/release/list`);
  }

  /* gets release number from currentUser objects */
  getRelease() {
	  return JSON.parse(sessionStorage.getItem('currentUser'))['release'];
  }

  /* sets release attribute in currentUser object iff newRelease > currentUser's release */
  setRelease(newRelease: number) {
	  var currentUser = JSON.parse(sessionStorage.getItem('currentUser'))
	  if (newRelease > currentUser['release']) {
		currentUser['release'] = newRelease;
		sessionStorage.setItem('currentUser', JSON.stringify(currentUser));
	  }
  }

  getUserVerified(){
    // API  call to get all the groups
    return this.httpClient.get(`system/userCheck/`)
  }


}
