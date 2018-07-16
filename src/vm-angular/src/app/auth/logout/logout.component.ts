import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})

// component that deals with user logout
export class LogoutComponent implements OnInit {

  constructor(private authService: AuthService, public router: Router) { }

  ngOnInit() {
  }
  
  // error flag (currently not used)
  error: boolean = false;
  
  deleteToken() {
	  this.authService.deleteToken().subscribe((response) => {
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
		  // console.log(error);
	  });
  }

}
