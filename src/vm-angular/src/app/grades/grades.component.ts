import { Component, OnInit } from '@angular/core';
import { GradesService } from './grades-service';

@Component({
  selector: 'app-grades',
  templateUrl: './grades.component.html',
  styleUrls: ['./grades.component.css']
})
export class GradesComponent implements OnInit {

  constructor(private gradesService: GradesService) { }

  list_comments: Array<object>;
  error: boolean = false;


  ngOnInit() {
    this.getGradesList();
    

  }

  public getGradesList(){
    this.gradesService.getGradesList().subscribe((data: Array<object>)=> {
      this.error = false;
    this.list_comments = data;

    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

}
