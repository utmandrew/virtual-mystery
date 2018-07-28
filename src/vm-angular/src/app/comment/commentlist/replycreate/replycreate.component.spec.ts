import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReplycreateComponent } from './replycreate.component';

describe('ReplycreateComponent', () => {
  let component: ReplycreateComponent;
  let fixture: ComponentFixture<ReplycreateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReplycreateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReplycreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
