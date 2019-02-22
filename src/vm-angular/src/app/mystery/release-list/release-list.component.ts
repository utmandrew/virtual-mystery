import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MysteryService } from '../mystery.service';
import { Release } from '../release.interface';

@Component({
  selector: 'app-release-list',
  templateUrl: './release-list.component.html',
  styleUrls: ['./release-list.component.css']
})
export class ReleaseListComponent implements OnInit {
	
  // list of releases
  public releases: Array<Release> = [];
  // error flag
  error: boolean = false;

  constructor(private mysteryService: MysteryService, public router: Router) { }

  ngOnInit() {
	  this.getReleases();
  }
  
  /* requests a list of current releases */
  public getReleases() {
	  this.mysteryService.listRelease().subscribe((data: Array<Release>) => {
		  this.releases = data;
		  // sends current release number to mysteryService
		  this.mysteryService.setRelease((this.releases[this.releases.length-1]).number);
		  this.error = false;
	  },
	  error => {
		  this.error = true;
	  });
  }
  
  /* Navigates to the selected release view component */
  public selectedRelease(release: number) {
	  this.router.navigate(['mystery/release', release]);
  }

}
