import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CommentcreateComponent } from './commentcreate.component';

describe('CommentcreateComponent', () => {
  let component: CommentcreateComponent;
  let fixture: ComponentFixture<CommentcreateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CommentcreateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CommentcreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
