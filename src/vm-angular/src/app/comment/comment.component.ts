import { Component, OnInit, Input } from '@angular/core';
import { CommentService } from './comment.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent implements OnInit {

  constructor(private commentService: CommentService) { }
  
  @Input() release: number;

  ngOnInit() {
	  this.commentService.setRelease(this.release);
  }

}
