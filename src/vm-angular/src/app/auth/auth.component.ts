import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})

/* Component that handles anything that has to do with user authorization*/
export class AuthComponent implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit() {
  }
  
  // form data
  model: any = {};
  // error flag
  error: boolean = false;
  
  getToken(){
	  // logs authentication info onto console (for testing only)
	  console.log(JSON.stringify(this.model));
	  this.authService.getToken(this.model).subscribe((response) => {
		  // logs response token onto console (for testing only)
		  console.log(response['token']);
		  this.error = false;
		  // sets current user token value into browsers session storage
		  sessionStorage.setItem('currentUser', JSON.stringify({ token: response['token'] }));
	  },
	  // sets error flag to true iff an error occurs with the request
	  error => {
		  this.error = true;
		  console.log(error);
	  });
  };

}
