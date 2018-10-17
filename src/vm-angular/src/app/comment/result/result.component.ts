import { Component, OnInit } from '@angular/core';
import { ResultService } from './result.service';
import { Subscription } from 'rxjs';
import { CommentService } from '../comment.service';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  constructor( private resultService: ResultService,private commentService: CommentService) { }
  private show_result = true;
  private error: boolean = false;
  private user_comment: Array<object>=[];
  private result : Array<object>=[];

  releaseSubscription: Subscription;

  ngOnInit() {
    
    this.getResult();

  }

  public toggleResult(){
    if (this.show_result){
      this.show_result=false;
    }else{
      this.show_result=true;
    }
  }


  public getResult(){
    this.resultService.getComment().subscribe((data: Array<object>)=> {
      this.error = false;
    this.result= data;

    console.log(data);
    },

    error => {
      // ann error on the API call
      console.log("hi");
      this.error=true;
    });

  }

 

  

}
