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

  // for the groups releases
  private groups_relases: Array<object>=[];
  private curr_release: number;

  private groups_comments: Array<object>=[];

  private user_comment: Array<object>=[];

  // the result for a student given by the t.a
  private result: any = {
    feedback: String,
    mark: Number,
    id:{},
  };

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
    this.getUsers(groupName);
    this.getGroupsRelases(groupName);
    this.chosen_group = groupName;
    this.chosen_user = "Choose User";
  }

  public chosenUser(userName){
    // now that a user is picked get his/her top-level to be marked
    this.chosen_user = userName;
    this.result.feedback = "";
    this.result.mark = 0;
    this.result.id = 0;


    this.getComment(userName);


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

  public getComment(userName){
    this.taService.getComment(userName).subscribe((data: Array<object>)=> {
      this.error = false;
    this.user_comment = data;
    console.log(data);
    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public getGroupsRelases(groupName){
    this.taService.getGroupsRelases(groupName).subscribe((data: Array<object>)=> {
      this.error = false;
    this.groups_relases = data;
    this.curr_release = data.length;
    console.log(data);
    console.log(this.curr_release);
    this.getGroupsComments(groupName, this.curr_release)
    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public getGroupsComments(groupName, release){
    this.taService.getGroupsComments(groupName, release).subscribe((data: Array<object>)=> {
      this.error = false;
    this.groups_comments = data;
    console.log(data);
    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public previousRelease(){
      this.curr_release = this.curr_release - 1;
      this.getGroupsComments(this.chosen_group, this.curr_release)
  }

  public nextRelease(){
      this.curr_release = this.curr_release + 1;
      this.getGroupsComments(this.chosen_group, this.curr_release)
  }

  /* toggles show_replies flag for CommentInterface object */
  /*public toggleReply(id) {
    var comment = this.groups_comments.find(c => c.id === id);
    if (comment) {
      if (comment.show_replies) {
        comment.show_replies = false;
      } else {
        comment.show_replies = true;
      }
    }
  }*/
  
  public sendResult(result){
    result.id = this.user_comment[0];
    console.log(this.user_comment[0]);
    this.taService.sendResult(result).subscribe((response)=>{
    });

  }

}
