import { TestBed, inject } from '@angular/core/testing';

import { CommentService } from './comment.service';
import { HttpClientModule } from '@angular/common/http';

describe('CommentService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [CommentService],
      imports: [
      HttpClientModule,
      ]
    });
  });

  it('should be created', inject([CommentService], (service: CommentService) => {
    expect(service).toBeTruthy();
  }));
});
