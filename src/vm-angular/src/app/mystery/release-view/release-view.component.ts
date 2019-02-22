import { Component, OnInit, OnDestroy } from '@angular/core';
import { Router, ActivatedRoute, ParamMap, NavigationEnd } from '@angular/router';
import { MysteryService } from '../mystery.service';
import { AuthService } from '../../auth/auth.service';
import {HttpClientModule} from '@angular/common/http';


@Component({
  selector: 'app-release-view',
  templateUrl: './release-view.component.html',
  styleUrls: ['./release-view.component.css']
})
export class ReleaseViewComponent implements OnInit, OnDestroy {

  error: boolean = false;


  constructor(private route: ActivatedRoute, private mysteryService: MysteryService, private authService: AuthService, public router: Router) {

	// subscribes to router events observable
	this.navigationSubscription = this.router.events.subscribe((e: any) => {
		// checks if navigation has ended
		if (e instanceof NavigationEnd) {
			this.initEvents();
		}
	});
  }

  // selected release
  public release: number;
  // router event observable subscription
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
  
  getMysteryRelease() {
	  // used in html
	  return this.mysteryService.getRelease();
  }

  public verifyUserType(){
    // used in html
    if (this.authService.getUser()){
      return this.authService.getUserType();
    } else{
      return false;
    }
  }


}
