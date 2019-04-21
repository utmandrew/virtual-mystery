import { Injectable } from '@angular/core';
import { HttpService } from '../http.service';


@Injectable({
  providedIn: 'root'
})
export class GradesService {
  API_URL = 'http://django:80';

  constructor(private httpClient: HttpService) { }
  
  /*
  Returns a list of comments for the logged in user
  - Comment objects have their results
  - Sort Comments by release number
  */
  getGradesList(){
    return this.httpClient.get(`${this.API_URL}/comment/userGrades`);

  }

  
  
}
