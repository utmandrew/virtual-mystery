import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { NO_ERRORS_SCHEMA } from '@angular/core';

import { MysteryComponent } from './mystery.component';

describe('MysteryComponent', () => {
  let component: MysteryComponent;
  let fixture: ComponentFixture<MysteryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MysteryComponent ],
      schemas: [ NO_ERRORS_SCHEMA ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MysteryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
