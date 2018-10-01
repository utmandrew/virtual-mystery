import { Component, OnInit, OnChanges, Input } from '@angular/core';
import { ArtifactserviceService } from './artifactservice.service';
import { HttpService } from '../http.service';
import { CommentComponent } from '../comment/comment.component';

@Component({
  selector: 'app-artifact-view',
  templateUrl: './artifact-view.component.html',
  styleUrls: ['./artifact-view.component.css']
})
export class ArtifactViewComponent implements OnInit, OnChanges {

  @Input() release: number;
  // error flag
  private error: boolean = false;
  private  release_data:  Array<object> = [];

  constructor(private artifactService: ArtifactserviceService ) { }

  ngOnInit() {
    this.getData(this.release);
  }
  
  /* Runs when release variable changes */
  ngOnChanges(release) {
	  this.getData(this.release);
  }
  
  /* Calls artifact service function getData with the inputted release and assigns the return value to data variable */
  public getData(release: number) {
    
    this.artifactService.getData(release).subscribe((data:  Array<object>) => {
        this.error = false;
		this.release_data  =  data;
    },
	error => {
		// an error occurred during api call
		this.error = true;
	});

  }

}
