import { Component, OnInit, OnChanges, Input } from '@angular/core';
import { CommentService } from './comment.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css'],
  providers: [CommentService]
})
export class CommentComponent implements OnInit, OnChanges {

  constructor(private commentService: CommentService) { }
  
  @Input() release: number;

  ngOnInit() {
	  this.commentService.setRelease(this.release);
  }
  
  /* Runs when release variable changes */
  ngOnChanges(release) {
	  this.commentService.setRelease(this.release);
  }
  
  getShowComments() {
	  // used in html
	  return this.commentService.showComments;
  }

}
