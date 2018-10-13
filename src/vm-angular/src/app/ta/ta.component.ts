import { Component, OnInit } from '@angular/core';
import { TAService } from './ta.service';

@Component({
  selector: 'app-ta',
  templateUrl: './ta.component.html',
  styleUrls: ['./ta.component.css']
})
export class TAComponent implements OnInit {
  
  private error: boolean = false;
  // for practicals
  private practical_data: Array<object>=[];
  private chosen_practical: string = "Choose Practical";
  // for groups
  private chosen_group: string = "Choose Group";
  private group_data: Array<object>= [];
  // for users
  private list_users: Array<object>= [];
  private chosen_user: string = "Choose User";

  constructor(private taService: TAService) { }

  ngOnInit() {
    // get all the Practicals in the course so far
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
    this.chosen_user = "Choose User";
  }

  public chosenUser(userName){
    // now that a user is picked get his/her top-level to be marked
    this.chosen_user = userName;
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
 
  public getUsers(groupName){
    this.taService.getUsers(groupName).subscribe((data: Array<object>)=> {
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
