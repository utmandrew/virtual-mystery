import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtifactViewComponent } from './artifact-view.component';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { HttpClientModule } from '@angular/common/http';


describe('ArtifactViewComponent', () => {
  let component: ArtifactViewComponent;
  let fixture: ComponentFixture<ArtifactViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArtifactViewComponent ],
       imports:[
           BrowserModule,
           FormsModule,
           ReactiveFormsModule,
           RouterTestingModule,
           HttpClientTestingModule,
           HttpClientModule,
       ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ArtifactViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
