import { Injectable } from '@angular/core';
import { HttpService,} from '../http.service';



@Injectable({
  providedIn: 'root'
})
export class ArtifactserviceService {

  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { 
  }

  getData() {
    // sends a request for a specific release and recieves a list of comments
    return this.httpClient.get(`${this.API_URL}/artifact-view/artifact-view`)
    
  }



}
