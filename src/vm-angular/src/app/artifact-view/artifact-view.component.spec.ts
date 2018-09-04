import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ArtifactViewComponent } from './artifact-view.component';

describe('ArtifactViewComponent', () => {
  let component: ArtifactViewComponent;
  let fixture: ComponentFixture<ArtifactViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ArtifactViewComponent ]
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
