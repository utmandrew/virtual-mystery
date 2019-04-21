import { Injectable } from '@angular/core';
import { HttpService } from '../http.service';


@Injectable({
  providedIn: 'root'
})
export class GradesService {

  constructor(private httpClient: HttpService) { }

  /*
  Returns a list of comments for the logged in user
  - Comment objects have their results
  - Sort Comments by release number
  */
  getGradesList(){
    return this.httpClient.get(`comment/userGrades`);

  }



}
