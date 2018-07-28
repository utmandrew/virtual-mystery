import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-not-found',
  template:
  `
	<div class="container h-100">
		<div class="row h-100 justify-content-center align-items-center" >
			<div><h4 class="font-italic" >404 Page Not Found</h4></div>
		</div>
	</div>
  `
})
export class NotFoundComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
