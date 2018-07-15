import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpRequest, HttpHandler, HttpEvent, HttpInterceptor, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable()

export class AuthInterceptor implements HttpInterceptor {

  constructor(public router: Router) {}
  
  intercept(request: HttpRequest<any>, next:HttpHandler): Observable<HttpEvent<any>> {
	
	return next.handle(request).pipe(tap((event: HttpEvent<any>) => {
		
	}, (err: any) => {
		
		if (err instanceof HttpErrorResponse) {
			if (err.status === 401) {
				// deletes currentUser from sessionStorage
				if (sessionStorage.getItem('currentUser')) {
					sessionStorage.removeItem('currentUser');
				}
				// redirect to the login route
				this.router.navigate(['auth']);
			}
		}
 
	}));
 
  }

}
