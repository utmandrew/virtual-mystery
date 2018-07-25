import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommentService } from '../comment.service';
import { Comment } from '../comment.interface';

@Component({
  selector: 'app-commentlist',
  templateUrl: './commentlist.component.html',
  styleUrls: ['./commentlist.component.css']
})
export class CommentlistComponent implements OnInit {

  constructor(private commentService: CommentService, public router: Router) { }

  ngOnInit() {
	  this.listComment(1);
  }
  
  // list of comments
  private comments: Array<Comment> = [];
  error: boolean = false;
  
  public listComment(release) {
	  // requests and displays mystery comments for a specific release
	  this.commentService.listComment(release).subscribe((data: Array<Comment>) => {
		  this.comments = data;
		  this.error = false;
	  },
	  error => {
		  if (error.status === 403) {
			  // redirect to comment create component
			  this.router.navigate(['comment/create']);
		  }
		  this.error = true
	  });
  }
  
  public toggleReply(id) {
	  // toggles show_replies flag for CommentInterface object
	  var comment = this.comments.find(c => c.id === id);
	  if (comment) {
		  if (comment.show_replies) {
			  comment.show_replies = false;
		  } else {
			  comment.show_replies = true;
		  }
	  }
  }
  
  private recieveReply($event) {
	  // finds parent comment and adds new reply
	  var comment = this.comments.find(c => c.id === $event[0]);
	  if (comment) {
		  comment.reply.push($event[1]);
	  }
  }

}
