import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HTTP_INTERCEPTORS } from '@angular/common/http';

// custom modules
import { AppRoutingModule } from './app-routing/app-routing.module';

// custom components
import { AppComponent } from './app.component';
import { AuthComponent } from './auth/auth.component';

// custom services/interceptors
import { AuthInterceptor } from './auth/auth.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    AuthComponent
  ],
  imports: [
    BrowserModule,
	HttpClientModule,
	AppRoutingModule,
	FormsModule,
	ReactiveFormsModule
  ],
  providers: [
	{
		provide: HTTP_INTERCEPTORS,
		useClass: AuthInterceptor,
		multi: true
	}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
