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
  private error : Boolean = false;
  // AuthService is used in the html
  constructor(private authService: AuthService, private mysteryService: MysteryService, public router: Router) {  
  
  // navigates to the current week
  currentClue() {
	  var release = this.mysteryService.getRelease();
    this.router.navigate(['mystery/release', release]);
  }

  public verifyUserType(){
    // used in html
    if (this.authService.getUser()){
      return this.authService.getUserType();
    } else{
      return false;
    }
  }
  
  getAuthUser() {
	  // Used in html
	  return this.authService.getUser();
  }

}
