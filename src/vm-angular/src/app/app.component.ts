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
  private is_ta : Array<object> = [];
  // AuthService is used in the html
  constructor(private authService: AuthService, private mysteryService: MysteryService, public router: Router) {  }
  



  ngOnInit() {
  this.getUserVerified();

  }
  ngOnChanges(){
    this.getUserVerified();

  }

  // navigates to the current week
  currentClue() {
	  var release = this.mysteryService.getRelease();
    this.router.navigate(['mystery/release', release]);
    this.getUserVerified();


  }
  
  public getUserVerified(){

    this.mysteryService.getUserVerified().subscribe((data: Array<object>)=> {
      this.error = false;
      this.is_ta = data;


    },

    error => {
      // ann error on the API call
      this.error=true;
    });

  }
}
