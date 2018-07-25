import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from '../auth/login/login.component';
import { CommentcreateComponent } from '../comment/commentcreate/commentcreate.component';

const routes: Routes = [
	{ path: '', redirectTo: 'auth', pathMatch: 'full' },
	{ path: 'auth', component: LoginComponent },
	{ path: 'comment/create', component: CommentcreateComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
