import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

// componenet that handels user login
export class LoginComponent implements OnInit {

  constructor(private authService: AuthService, public router: Router) { }

  ngOnInit() {
  }

  // form data
  model: any = {};
  // error flag
  error: boolean = false;

  getToken(){

	  this.authService.getToken(this.model).subscribe((response) => {

		  // sets error flag
		  this.error = false;

		  // sets current user token value into browsers session storage
		  sessionStorage.setItem('currentUser', JSON.stringify({ token: response['token'], 
																 release: response['release'], 
																 mark: response['mark'],
																 mystery_end: response['mystery_end'],
																 is_ta: response['is_ta']}));

		  // redirect to current release view

		if (response['is_ta']){

			this.router.navigate(['taview']);
		} else{
		  this.router.navigate(['mystery/release/list']);
		}
	  },
	  // sets error flag to true iff an error occurs with the request
	  error => {
		  this.error = true;

	  });
  };




}
