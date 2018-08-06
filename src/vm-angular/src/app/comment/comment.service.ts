import { Injectable } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpService } from '../http.service';

@Injectable()

/* Service that allows access to all of comment component functions dealing with api */
export class CommentService {
  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }
  
  // show comments flag
  showComments: boolean = true;
  // release number
  // release: number;
  private release = new BehaviorSubject<number>(0);
  
  createComment(data) {
	  // sends comment data to create a new comment
	  return this.httpClient.post(`${this.API_URL}/comment/create`,data);
  }
  
  createReply(data) {
	  // sends reply data to create a new reply
	  return this.httpClient.post(`${this.API_URL}/comment/reply`,data);
  }
  
  listComment(release) {
	  // sends a request for a specific release and recieves a list of comments
	  return this.httpClient.get(`${this.API_URL}/comment/${release}`)
  }
  
  /* setRelease(newRelease: number) {
	  this.release = newRelease;
  } */
  
  setRelease(newRelease: number) {
	  console.log("set: ", newRelease);
	  this.release.next(newRelease);
  }
  
  /* getRelease() {
	  return this.release;
  } */
  
  getRelease(): Observable<number> {
	  return this.release.asObservable();
  }
  
}
