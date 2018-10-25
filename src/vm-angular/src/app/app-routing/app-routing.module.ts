import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from '../auth/login/login.component';
import { MysteryComponent } from '../mystery/mystery.component';
import { ReleaseViewComponent } from '../mystery/release-view/release-view.component';
import { ReleaseListComponent } from '../mystery/release-list/release-list.component';
import { NotFoundComponent } from '../not-found.component';
import { AuthGuardService } from '../auth/auth-guard.service';
import { GradesComponent } from '../grades/grades.component';
import { TAComponent } from '../ta/ta.component';

const routes: Routes = [
	{ path: '', redirectTo: 'auth', pathMatch: 'full' },
	{ path: 'auth', component: LoginComponent },
	{
		path: 'mystery',
		children: [
			{ path: 'release/list', component: ReleaseListComponent },

			// Make sure release/:id is the last path!
			{ path: 'release/:id', component: ReleaseViewComponent },
		],
		canActivate: [AuthGuardService],
		runGuardsAndResolvers: 'always'
	},
	{ path: 'grades', component: GradesComponent , canActivate: [AuthGuardService], runGuardsAndResolvers: 'always'},

	{path: 'taview', component: TAComponent, canActivate: [AuthGuardService], runGuardsAndResolvers: 'always'},

	// Make sure ** is the last path!
	{ path: '**', component: NotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {onSameUrlNavigation: 'reload'})],
  exports: [RouterModule]
})
export class AppRoutingModule { }
