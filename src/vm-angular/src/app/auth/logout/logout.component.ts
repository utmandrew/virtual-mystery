import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit() {
  }
  
  // error flag
  error: boolean = false;
  
  deleteToken() {
	  this.authService.deleteToken().subscribe((response) => {
		  sessionStorage.removeItem('currentUser');
		  this.error = false;
	  },
	  // sets error flag to true iff an error occurs with the request
	  error => {
		  this.error = true;
		  console.log(error);
	  });
  }

}
