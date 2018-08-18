import { Component, OnInit } from '@angular/core';
import { ArtifactserviceService } from './artifactservice.service';
import { HttpService } from '../http.service';
import { CommentComponent } from '../comment/comment.component';





@Component({
  selector: 'app-artifact-view',
  templateUrl: './artifact-view.component.html',
  styleUrls: ['./artifact-view.component.css']
})
export class ArtifactViewComponent implements OnInit {


  private  contacts:  Array<object> = [];
  private image : string;


  constructor(private artifactService: ArtifactserviceService ) { }

  ngOnInit() {
    this.getData();
  }
  
  public  getData(){
    /// data is the data returned from the backend
  
    this.artifactService.getData().subscribe((data:  Array<object>) => {
        this.contacts  =  data;


        console.log(data);
    });

  }



}
