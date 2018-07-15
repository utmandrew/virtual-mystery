import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  // authenticated user flag (default = false)
  user: boolean = false;
  
  constructor() {
	// sets user flag
	if (sessionStorage.getItem('currentUser')) {
		this.user = true;
	} else {
		this.user = false;
	}
  }
  
}
