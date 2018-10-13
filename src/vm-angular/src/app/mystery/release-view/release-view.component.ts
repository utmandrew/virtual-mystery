import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute, ParamMap, NavigationEnd } from '@angular/router';
import { MysteryService } from '../mystery.service';


@Component({
  selector: 'app-release-view',
  templateUrl: './release-view.component.html',
  styleUrls: ['./release-view.component.css']
})
export class ReleaseViewComponent implements OnInit, OnDestroy {

  private error: boolean = false;
  private is_ta: Array<object> = [];


  constructor(private route: ActivatedRoute, private mysteryService: MysteryService, public router: Router) { 

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
  // router event observable subscription
  navigationSubscription;
  
  ngOnInit() {
	  // Gets release id from url
	  this.route.paramMap.subscribe((params: ParamMap) => { 
		this.release = parseInt(params.get('id'));
    });
    this.getUserVerified();


  }
  
  /* Runs when component instance is destroyed */
  ngOnDestroy() {
	  if (this.navigationSubscription) {
		  // unsubscribes from router events to avooid memory leaks
		  this.navigationSubscription.unsubscribe();
	  }
  }
  
  /* Runs component re-initialization commands */
  initEvents() {
	  // Gets release id from url
	  this.route.paramMap.subscribe((params: ParamMap) => { 
		this.release = parseInt(params.get('id'));
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

  public getUserVerified(){

    this.mysteryService.getUserVerified().subscribe((data: Array<object>)=> {
      this.error = false;
    this.is_ta = data;
    console.log(data);
    },

    error => {
      // ann error on the API call
      this.error=true;
    });

  }
  

}
