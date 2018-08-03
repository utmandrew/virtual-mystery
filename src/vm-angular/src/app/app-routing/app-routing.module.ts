import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from '../auth/login/login.component';
import { CommentcreateComponent } from '../comment/commentcreate/commentcreate.component';
import { CommentlistComponent } from '../comment/commentlist/commentlist.component';
import { ArtifactViewComponent } from '../artifact-view/artifact-view.component';
import { NotFoundComponent } from '../not-found.component';

const routes: Routes = [
	{ path: '', redirectTo: 'auth', pathMatch: 'full' },
	{ path: 'auth', component: LoginComponent },
	{ path: 'comment/create', component: CommentcreateComponent },
	{ path: 'comment/list', component: CommentlistComponent },
	{ path: 'hello/hello-view', component: ArtifactViewComponent },

	// Make sure ** is the last path!
	{ path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
