import { Injectable } from '@angular/core';
import { HttpService} from '../http.service';

@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all artifactview component functions dealing with api */
export class TAService {


  API_URL = 'http://localhost:8000';
  ASSETS_URL = this.API_URL + '/assets/';

  constructor(private httpClient: HttpService) { }

  getPracticals() {
    // Call to get all the PRacticals
    return this.httpClient.get(`${this.API_URL}/system/practicals/`)
  }

  getGroups(name: string){
    // Call to get all the groups
    return this.httpClient.get(`${this.API_URL}/system/groups/${name}`)
  }

  getUsers(groupId: number){
    // Call to retrieve all users in groupName
    return this.httpClient.get(`${this.API_URL}/system/users/${groupId}`)
  }

  getComment(userName: string){
    // Get the top level comments made by a user for this week
    return this.httpClient.get(`${this.API_URL}/system/userComment/${userName}`)
  }

  getGroupsRelases(groupId: number){
    return this.httpClient.get(`${this.API_URL}/mystery/release/group/${groupId}`)
  }

  getGroupsComments(groupId, release){
    return this.httpClient.get(`${this.API_URL}/comment/${release}/${groupId}`)
  }

  sendResult(data){
    return this.httpClient.post(`${this.API_URL}/comment/resultCreate`,data);
  }

  createTaComment(data){
    return this.httpClient.post(`${this.API_URL}/comment/taCreate`,data);
  }


}
