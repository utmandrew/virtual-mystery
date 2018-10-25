import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { MysteryService } from './mystery/mystery.service';
import { AuthService } from './auth/auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  
  // AuthService is used in the html
  constructor(private authService: AuthService, private mysteryService: MysteryService, public router: Router) {  }
  
  // navigates to the current week
  currentClue() {
	  var release = this.mysteryService.getRelease();
	  this.router.navigate(['mystery/release', release]);
  }
  
  getAuthUser() {
	  // Used in html
	  return this.authService.getUser();
  }
  
}
