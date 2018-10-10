import { Component, OnInit } from '@angular/core';
import {  FileUploader, FileSelectDirective } from 'ng2-file-upload/ng2-file-upload';
import { Observable, BehaviorSubject } from 'rxjs';
import { HttpService } from '../http.service';


const URL = 'http://localhost:8000/comment/upload';

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

  onFileChanged(event) {
    this.selectedFile = event.target.files[0];
  }

  onUpload() {
  // this.http is the injected
  console.log(this.selectedFile)
this.httpClient.post(`${this.API_URL}/comment/upload`, this.selectedFile)
.subscribe(...);
  }

}
