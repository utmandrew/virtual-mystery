import { TestBed, inject } from '@angular/core/testing';

import { MysteryService } from './mystery.service';
import { HttpClientModule } from '@angular/common/http';

describe('MysteryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MysteryService],
      imports: [
      HttpClientModule,
      ]
    });
  });

  it('should be created', inject([MysteryService], (service: MysteryService) => {
    expect(service).toBeTruthy();
  }));
});
