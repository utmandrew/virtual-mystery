import { Component, OnInit } from '@angular/core';
import { GradesService } from './grades-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-grades',
  templateUrl: './grades.component.html',
  styleUrls: ['./grades.component.css']
})
export class GradesComponent implements OnInit {

  constructor(private gradesService: GradesService, public router: Router) { }

  list_comments: Array<object>;
  error: boolean = false;


  ngOnInit() {
    this.getGradesList();
    

  }

  public getGradesList(){
    this.gradesService.getGradesList().subscribe((data: Array<object>)=> {
      this.error = false;
    this.list_comments = data;
    console.log(data);
    

    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public selectedRelease(release: number) {
	  this.router.navigate(['mystery/release', release]);
  }

}
