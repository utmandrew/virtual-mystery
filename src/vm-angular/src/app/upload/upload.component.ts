import { Component, OnInit } from '@angular/core';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpService } from '../http.service';


@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css']
})
export class UploadComponent implements OnInit {



  API_URL = 'http://localhost:8000';

  constructor(private httpClient: HttpService) { }

  ngOnInit() {
  }

  selectedFile: File;

  //saves the file you selected to temp var
  onFileChanged(event) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
  console.log(this.selectedFile);
  //sends the file you selected to the Django upload endpoint
  this.httpClient.post(`${this.API_URL}/upload/${this.selectedFile.name}`, this.selectedFile).subscribe(...);
  }

}
