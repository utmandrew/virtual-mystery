import { Injectable } from '@angular/core';
import { HttpService } from '../../http.service';


@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all artifactview component functions dealing with api */
export class ResultService {


  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }

  getComment(release: string){


  }

}
