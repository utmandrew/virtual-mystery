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
  
  ngOnChanges(release) {
	  console.log("change: ", this.release);
	  this.commentService.setRelease(this.release);
  }

}
