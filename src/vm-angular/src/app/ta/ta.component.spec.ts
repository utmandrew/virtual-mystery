import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TAComponent } from './ta.component';

describe('TAComponent', () => {
  let component: TAComponent;
  let fixture: ComponentFixture<TAComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TAComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TAComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
