import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpService } from '../http.service';
import { HttpClientModule } from '@angular/common/http';
import { HttpModule } from '@angular/http';
@Injectable()



export class UploadService {

  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }


  upload(data) {
    // sends comment data to create a new comment
    return this.httpClient.post(`${this.API_URL}/upload`,data);
  }

}
