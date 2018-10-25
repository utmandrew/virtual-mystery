import { Component, OnInit } from '@angular/core';
import { ResultViewService } from 'src/app/mystery/release-view/result-view/result-view-service';
import { CommentService } from '../../../comment/comment.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-result-view',
  templateUrl: './result-view.component.html',
  styleUrls: ['./result-view.component.css']
})
export class ResultViewComponent implements OnInit {

  constructor( private resultViewService: ResultViewService) { }
  private show_result = true;
  private error: boolean = false;
  private user_comment: Array<object>=[];
  private result : Array<object>=[];


  
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
    this.resultViewService.getComment().subscribe((data: Array<object>)=> {
      this.error = false;
    this.result= data;


    },

    error => {
      // ann error on the API call

      this.error=true;
    });

  }

  

}
