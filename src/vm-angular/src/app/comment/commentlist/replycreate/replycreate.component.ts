import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { CommentService } from '../../comment.service';
import { Reply } from '../../reply.interface';

@Component({
  selector: 'app-replycreate',
  templateUrl: './replycreate.component.html',
  styleUrls: ['./replycreate.component.css']
})
export class ReplycreateComponent implements OnInit {

  constructor(private commentService: CommentService) { }

  ngOnInit() {
  }
  
  @Input() parentId: string;
  @Output() replyEvent = new EventEmitter<Array<any>>();
  
  // reply
  model: any = {};
  // error flag
  error: boolean = false;
  
  public sendReply(reply: Reply) {
	  // sends new reply and parent id to commentlist component
	  this.replyEvent.emit([this.parentId, reply]);
  }
  
  /* creates user reply with info in model and parentId variables */
  public createReply() {
	  this.model.parent = this.parentId;
	  this.commentService.createReply(this.model).subscribe((data: Reply) => {
		 this.sendReply(data);
		 // clear text box
		 this.model.text = '';
		 this.error = false; 
	  },
	  error => {
		  this.error = true;
	  });
  }
  
}
