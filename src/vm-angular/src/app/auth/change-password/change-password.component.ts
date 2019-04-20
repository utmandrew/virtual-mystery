import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrls: ['./change-password.component.css']
})
export class ChangePasswordComponent implements OnInit {

  constructor(private authService: AuthService, public router: Router) { }

  ngOnInit() {
  }
  
  // form data
  model: any = {};
  // error flag
  error: boolean = false;
  
  changePassword(){

	  this.authService.changePassword(this.model).subscribe((response) => {

		  // removes current user info from session storage
		  sessionStorage.removeItem('currentUser');
		  // sets error flag
		  this.error = false;
		  // redirects user to login page
		  this.router.navigate(['auth']);

	  },
	  // sets error flag to true iff an error occurs with the request
	  error => {
		  this.error = true;
	  });
  };

}
