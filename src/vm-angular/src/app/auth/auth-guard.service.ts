import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})

// authentication guard for routes which require user to be logged in
export class AuthGuardService implements CanActivate {

  constructor(private authService: AuthService, public router: Router) { }
  
  // required to implement CanActivate interface
  canActivate(): boolean {
	  if (!this.authService.getUser()) {
		  this.router.navigate(['auth']);
		  return false;
	  }
	  return true;
  }
  
}
