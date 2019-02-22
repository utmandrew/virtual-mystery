import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { NO_ERRORS_SCHEMA } from '@angular/core';

import { CommentlistComponent } from './commentlist.component';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { Routes, RouterModule } from '@angular/router';
import { RouterTestingModule } from '@angular/router/testing';

describe('CommentlistComponent', () => {
  let component: CommentlistComponent;
  let fixture: ComponentFixture<CommentlistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CommentlistComponent ],
      imports:[
          BrowserModule,
          FormsModule,
          ReactiveFormsModule,
          HttpClientModule,
          RouterModule,
          RouterTestingModule
      ],
      schemas: [ NO_ERRORS_SCHEMA ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CommentlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
