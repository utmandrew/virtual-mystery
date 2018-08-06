import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute, ParamMap, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-release-view',
  templateUrl: './release-view.component.html',
  styleUrls: ['./release-view.component.css']
})
export class ReleaseViewComponent implements OnInit, OnDestroy {

  constructor(private route: ActivatedRoute, public router: Router) { 
	// subscribes to router events observable
	this.navigationSubscription = this.router.events.subscribe((e: any) => {
		// checks if navigation has ended
		if (e instanceof NavigationEnd) {
			this.initEvents();
		}
	});
  }

  // selected release
  private release: number;
  navigationSubscription;
  
  ngOnInit() {
	  // Gets release id from url
	  this.route.paramMap.subscribe((params: ParamMap) => { 
		this.release = parseInt(params.get('id'));
	  });
  }
  
  /* Runs when component instance is destroyed */
  ngOnDestroy() {
	  if (this.navigationSubscription) {
		  // unsubscribes from router events to avooid memory leaks
		  this.navigationSubscription.unsubscribe();
	  }
  }
  
  initEvents() {
	  // Gets release id from url
	  this.route.paramMap.subscribe((params: ParamMap) => { 
		this.release = parseInt(params.get('id'));
		console.log(this.release);
	  });
  }
  
  /* navigates to the next release */
  nextRelease() {
	    this.router.navigate(['mystery/release', this.release + 1]);
  }
  
  /* navigates to the previous release */
  previousRelease() {
	  if (this.release > 1) {
		this.router.navigate(['mystery/release', this.release - 1]);
	  }
  }

}
