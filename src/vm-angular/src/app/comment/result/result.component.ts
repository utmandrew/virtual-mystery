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
  releaseSubscription: Subscription;

  ngOnInit() {
    this.releaseSubscription = this.commentService.getRelease().subscribe((release: number) => {

    })
  }

  public toggleResult(){
    if (this.show_result){
      this.show_result=false;
    }else{
      this.show_result=true;
    }
  }

 

  

}
