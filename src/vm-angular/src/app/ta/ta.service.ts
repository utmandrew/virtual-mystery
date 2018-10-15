import { Injectable } from '@angular/core';
import { HttpService} from '../http.service';

@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all artifactview component functions dealing with api */
export class TAService {


  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }

  getPracticals() {
    // Call to get all the PRacticals
    return this.httpClient.get(`${this.API_URL}/system/practicals/`)
  }

  getGroups(name: string){
    // Call to get all the groups
    return this.httpClient.get(`${this.API_URL}/system/groups/${name}`)
  }

  getUsers(groupName: string){
    // Call to retrieve all users in groupName
    return this.httpClient.get(`${this.API_URL}/system/users/${groupName}`)
  }

  getComment(userName: string){
    // Get the top level comments made by a user for this week
    return this.httpClient.get(`${this.API_URL}/system/userComment/${userName}`)
  }

  getGroupsRelases(groupName: string){
    return this.httpClient.get(`${this.API_URL}/mystery/release/${groupName}`)
  }


}
