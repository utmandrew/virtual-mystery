import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

// componenet that handels user login
export class LoginComponent implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit() {
  }
  
  // form data
  model: any = {};
  // error flag
  error: boolean = false;
  
  getToken(){
	  // logs authentication info onto console (for testing only)
	  // console.log(JSON.stringify(this.model));
	  
	  this.authService.getToken(this.model).subscribe((response) => {
		  
		  // logs response token onto console (for testing only)
		  // console.log(response['token']);
		  
		  // sets error flag
		  this.error = false;
		  
		  // sets current user token value into browsers session storage
		  sessionStorage.setItem('currentUser', JSON.stringify({ token: response['token'] }));
	  },
	  // sets error flag to true iff an error occurs with the request
	  error => {
		  this.error = true;
		  // console.log(error);
	  });
  };

}
