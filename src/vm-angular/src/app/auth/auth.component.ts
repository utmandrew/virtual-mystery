import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { UserService } from '../user.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {

  constructor(private authService: AuthService, private userService: UserService) { }

  ngOnInit() {
  }
  
  model: any = {};
  error: boolean = false;
  
  getToken(){
	  // logs authentication info onto console (for testing only)
	  console.log(JSON.stringify(this.model));
	  this.authService.getToken(this.model).subscribe((response) => {
		  // logs response token onto console (for testing only)
		  console.log(response['token']);
		  this.error = false;
		  // sets current user token value
		  this.userService.setToken(response['token'])
	  },
	  // sets error flag to true iff an error occurs with the request
	  error => this.error = true);
  };

}
