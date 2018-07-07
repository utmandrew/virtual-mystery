import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css']
})
export class AuthComponent implements OnInit {

  constructor(private authService: AuthService) { }

  ngOnInit() {
  }
  
  model: any = {};
  
  getToken(){
	  console.log(JSON.stringify(this.model));
	  this.authService.getToken(this.model).subscribe((response) => {
		  console.log(response);
	  });
  };

}
