import { Component, OnInit } from '@angular/core';
import { TAService } from './ta.service';

@Component({
  selector: 'app-ta',
  templateUrl: './ta.component.html',
  styleUrls: ['./ta.component.css']
})
export class TAComponent implements OnInit {


  error: boolean = false;
  // for practicals
  practical_data: Array<object>=[];
  chosen_practical: string;
  // for groups
  chosen_group: number;
  group_data: Array<object>= [];
  // for users
  list_users: Array<object>= [];
  chosen_user: string;

  // for the groups releases
  groups_relases: Array<object>=[];
  curr_release: number;

  groups_comments: Array<object>=[];

  user_comment: Array<object>=[];

  edit: Boolean = false;


  // the result for a student given by the t.a
  private result: any = {
    feedback: String,
    mark: Number,
    id: Number,
  };

  private taComment: any = {
    release: Number,
    mystery: Number,
    text: String,
    group: Number,
  };

  constructor(private taService: TAService) { }

  ngOnInit() {
    // get all the Practicals in the course so far
    this.chosen_practical="Choose Practical";
    this.chosen_group= 0;
    this.chosen_user = "Choose User";
    this.result.feedback = "";
    this.result.mark = 0;
    this.result.id = 0;
    this.getPracticals();
  }

  reinitialize(){
    this.chosenUser(this.chosen_user);
    // this.chosen_practical="Choose Practical";
    // this.chosen_group="Choose Group";
    // this.chosen_user = "Choose User";
    this.result.feedback = "";
    this.result.mark = 0;
    this.result.id = 0;

  }

  public chosenPractical(praName){
    this.getGroups(praName);
    this.chosen_practical = praName;
    this.chosen_group = 0;
  }

  public chosenGroup(groupId){
    this.getUsers(groupId);
    this.getGroupsRelases(groupId);
    this.chosen_group = groupId;
    this.chosen_user = "Choose User";
  }

  public chosenUser(userName){
    // now that a user is picked get his/her top-level to be marked
    this.chosen_user = userName;
    this.result.feedback = "";
    this.result.mark = 0;
    this.result.id = 0;


  }

  public getPracticals(){
    this.taService.getPracticals().subscribe((data: Array<object>)=> {
      this.error = false;
    this.practical_data = data;

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


    },

    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public getUsers(groupId){
    this.taService.getUsers(groupId).subscribe((data: Array<object>)=> {
      this.error = false;
    this.list_users = data;

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

    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public getGroupsRelases(groupId){
    this.taService.getGroupsRelases(groupId).subscribe((data: Array<object>)=> {
      this.error = false;

    this.groups_relases = data;
    this.curr_release = data.length;


    this.getGroupsComments(groupId, this.curr_release);
    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public getGroupsComments(groupId, release){
    this.taService.getGroupsComments(groupId, release).subscribe((data: Array<object>)=> {
      this.error = false;
    this.groups_comments = data;
    this.taComment.text = '';

    },
    error => {
      // ann error on the API call
      this.error=true;
    });
  }

  public previousRelease(){
      this.curr_release = this.curr_release - 1;
      this.getGroupsComments(this.chosen_group, this.curr_release);
  }

  public nextRelease(){
      this.curr_release = this.curr_release + 1;
      this.getGroupsComments(this.chosen_group, this.curr_release);
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

  public sendResult(result, id){
    result.id = id;




    this.taService.sendResult(result).subscribe((response)=>{
      this.error = false;
      //this.reinitialize();
      this.getGroupsComments(this.chosen_group, this.curr_release);

    },
    error => {
      if(error.status === 400){
        this.chosenUser(this.chosen_user);

      }
      this.error = true;
    }

    );

    //this.chosenUser(this.chosen_user);



  }

  public createTaComment(release, mystery){
    this.taComment.release = release;
    this.taComment.mystery = mystery;
    this.taComment.group = this.chosen_group;

    this.taService.createTaComment(this.taComment).subscribe((response)=>{
      this.error = false;
      //this.reinitialize();
      this.getGroupsComments(this.chosen_group, this.curr_release);
      this.taComment.text = '';
    },
    error => {
      if(error.status === 400){
        this.chosenPractical(this.chosen_practical);

      }
      this.error = true;
    }

    );



  }

  public toggleEdit(feedback, mark, id){
    this.result.id = id;
    if (this.edit == false){
      this.edit = true;
    }else{
      this.edit = false;
    }
  }
  public selectEdit(feedback,mark){
    this.result.feedback = feedback;
    this.result.mark = mark;

  }

}
