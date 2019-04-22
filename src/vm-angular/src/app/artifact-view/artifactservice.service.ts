import { Injectable } from '@angular/core';
import { HttpService} from '../http.service';

@Injectable({
  providedIn: 'root'
})

/* Service that allows access to all artifactview component functions dealing with api */
export class ArtifactserviceService {

  API_URL = '/api';
  ASSETS_URL = this.API_URL + '/static/mystery';

  constructor(private httpClient: HttpService) { }

  getData(release: number) {
    // sends a request for a specific release and recieves release info
    return this.httpClient.get(`${this.API_URL}/mystery/release/${release}`)
  }

}
