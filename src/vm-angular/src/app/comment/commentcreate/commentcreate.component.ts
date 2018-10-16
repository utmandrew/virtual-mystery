import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommentService } from '../comment.service';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-commentcreate',
  templateUrl: './commentcreate.component.html',
  styleUrls: ['./commentcreate.component.css']
})

/* component for creating a user comment */
export class CommentcreateComponent implements OnInit, OnDestroy {
	
  // release number
  release: number;
  // commentservice release observable subscription
  releaseSubscription: Subscription;
  // comment
  model: any = {};
  // error flag
  error: boolean = false;

  constructor(private commentService: CommentService) { }
  
  ngOnInit() {
	  this.releaseSubscription = this.commentService.getRelease().subscribe((release: number) => {
		if (this.release) {
			// release value change
			this.commentService.showComments = true;
		} else {
			// release value initialization
			this.release = release;
		}
	})
  }
  
  ngOnDestroy() {
	  // ensures no memory leaks
	  if (this.releaseSubscription) {
		  this.releaseSubscription.unsubscribe();
	  }
  }
   
   /* creates user comment with comment info in model variable */
   public createComment() {
	   this.commentService.createComment(this.model).subscribe((response) => {
		   // redirect to comment list component
		   this.commentService.showComments = true;
		   
		   this.error = false;
	   },
	   error => {
		   if (error.status === 403) {
			   // 403 indicates that user has already submitted a comment
			   
			   // redirect to comment list component
			   this.commentService.showComments = true;
			   
		   }
		   
		   this.error = true;
		   
	   })
	   
   }
   
}
