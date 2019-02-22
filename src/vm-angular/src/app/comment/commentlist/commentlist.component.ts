import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { CommentService } from '../comment.service';
import { Comment } from '../comment.interface';


@Component({
  selector: 'app-commentlist',
  templateUrl: './commentlist.component.html',
  styleUrls: ['./commentlist.component.css']
})
export class CommentlistComponent implements OnInit {

  // commentservice release observable subscription
  releaseSubscription: Subscription;
  // list of comments
  private comments: Array<Comment> = [];
  // error flag
  error: boolean = false;
  private show_result = true;

  private user_comment: Array<object>=[];
  private result : Array<object>=[];



  constructor(private commentService: CommentService, ) { }

  ngOnInit() {
	// subscribes to the commentService release value observable
	this.releaseSubscription = this.commentService.getRelease().subscribe((release: number) => {
		this.listComment(release);
	})
	


  }


 

  ngOnDestroy() {
	  // ensures no memory leaks
	  if (this.releaseSubscription) {
		  this.releaseSubscription.unsubscribe();
	  }
  }

  /* requests and displays instance comments for a specific release */
  public listComment(release) {
	  this.commentService.listComment(release).subscribe((data: Array<Comment>) => {
		  this.comments = data;

		  this.error = false;
	  },
	  error => {
		  if (error.status === 403) {
			  // 403 indicates that user has not submitted a comment

			  // redirect to comment create component
			  this.commentService.showComments = false;
		  }
		  this.error = true
	  });
  }

  /* toggles show_replies flag for CommentInterface object */
  public toggleReply(id) {
	  var comment = this.comments.find(c => c.id === id);
	  if (comment) {
		  if (comment.show_replies) {
			  comment.show_replies = false;
		  } else {
			  comment.show_replies = true;
		  }
	  }
  }

  /* recieves newly created reply from replycreate component and adds it to it's parent comment reply list*/
  private recieveReply($event) {
	  var comment = this.comments.find(c => c.id === $event[0]);
	  if (comment) {
		  comment.reply.push($event[1]);
	  }
  }
  
  getComments() {
	  // used in html
	  return this.comments;
  }
  
}
