import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ReleaseViewComponent } from './release-view.component';

describe('ReleaseViewComponent', () => {
  let component: ReleaseViewComponent;
  let fixture: ComponentFixture<ReleaseViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ReleaseViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ReleaseViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
