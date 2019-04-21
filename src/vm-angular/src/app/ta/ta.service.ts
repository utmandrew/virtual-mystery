import { Injectable } from '@angular/core';
import { HttpService} from '../http.service';

@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all artifactview component functions dealing with api */
export class TAService {


  API_URL = 'http://django:80';
  ASSETS_URL = this.API_URL + '/static/mystery';

  constructor(private httpClient: HttpService) { }

  getPracticals() {
    // Call to get all the PRacticals
    return this.httpClient.get(`system/practicals/`)
  }

  getGroups(name: string){
    // Call to get all the groups
    return this.httpClient.get(`system/groups/${name}`)
  }

  getUsers(groupId: number){
    // Call to retrieve all users in groupName
    return this.httpClient.get(`system/users/${groupId}`)
  }

  getComment(userName: string){
    // Get the top level comments made by a user for this week
    return this.httpClient.get(`system/userComment/${userName}`)
  }

  getGroupsRelases(groupId: number){
    return this.httpClient.get(`mystery/release/group/${groupId}`)
  }

  getGroupsComments(groupId, release){
    return this.httpClient.get(`comment/${release}/${groupId}`)
  }

  sendResult(data){
    return this.httpClient.post(`comment/resultCreate`,data);
  }

  createTaComment(data){
    return this.httpClient.post(`comment/taCreate`,data);
  }


}
