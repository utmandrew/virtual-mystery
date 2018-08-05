import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
  selector: 'app-release-view',
  templateUrl: './release-view.component.html',
  styleUrls: ['./release-view.component.css']
})
export class ReleaseViewComponent implements OnInit {

  constructor(private route: ActivatedRoute, public router: Router) { }

  // selected release
  private release: number;
  
  ngOnInit() {
	  // Gets release id from url
	  this.route.paramMap.subscribe((params: ParamMap) => { 
		this.release = parseInt(params.get('id'));
	  });
  }

}
