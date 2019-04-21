import { Injectable } from '@angular/core';
import { HttpService } from '../../../http.service';



@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all artifactview component functions dealing with api */
export class ResultViewService {



  constructor(private httpClient: HttpService) { }

  getComment(){
    return this.httpClient.get(`comment/userResult`);
  }

}
