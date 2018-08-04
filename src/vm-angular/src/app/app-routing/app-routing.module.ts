import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from '../auth/login/login.component';
import { CommentComponent } from '../comment/comment.component';
import { CommentcreateComponent } from '../comment/commentcreate/commentcreate.component';
import { CommentlistComponent } from '../comment/commentlist/commentlist.component';
import { NotFoundComponent } from '../not-found.component';

const routes: Routes = [
	{ path: '', redirectTo: 'auth', pathMatch: 'full' },
	{ path: 'auth', component: LoginComponent },
	{
		path: 'comment/:release',
		component: CommentComponent,
		children: [
			{ path: '', redirectTo: 'list', pathMatch: 'full' },
			{ path: 'create', component: CommentcreateComponent },
			{ path: 'list', component: CommentlistComponent },
		]
	},
	{ path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
