import { Component, OnInit } from '@angular/core';
import { TAService } from './ta.service';

@Component({
  selector: 'app-ta',
  templateUrl: './ta.component.html',
  styleUrls: ['./ta.component.css']
})
export class TAComponent implements OnInit {
  
  private error: boolean = false;
  private practical_data: Array<object>=[];
  private chosen_practical: string = "Choose Practical";
  private chosen_group: string = "Choose Group";
  private group_data: Array<object>= [];
  private list_users: Array<object>= [];

  constructor(private taService: TAService) { }

  ngOnInit() {
    this.getPracticals();
  }

  public chosenPractical(praName){
    this.getGroups(praName);
    this.chosen_practical = praName;
    this.chosen_group = "Choose Group";
  }

  public chosenGroup(groupName){
    this.getGroups(groupName);
    this.chosen_group = groupName;
  
  }
  

  public getPracticals(){
    this.taService.getPracticals().subscribe((data: Array<object>)=> {
      this.error = false;
    this.practical_data = data;
    console.log(data);
    },

    error => {
      // ann error on the API call
      this.error=true;
    });
  }


  // after click on a practical
  public getGroups(praName){
    this.taService.getGroups(praName).subscribe((data: Array<object>)=> {
      this.error = false;
    this.group_data = data;

     
    console.log(data);
    },

    error => {
      // ann error on the API call
      this.error=true;
    });
  }
 
  public getGroupView(groupName){
    this.taService.getGroups(groupName).subscribe((data: Array<object>)=> {
      this.error = false;
    this.list_users = data;
    console.log(data);
    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

}
