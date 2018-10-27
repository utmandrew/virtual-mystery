import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TaInstructionsComponent } from './ta-instructions.component';

describe('TaInstructionsComponent', () => {
  let component: TaInstructionsComponent;
  let fixture: ComponentFixture<TaInstructionsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TaInstructionsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TaInstructionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
