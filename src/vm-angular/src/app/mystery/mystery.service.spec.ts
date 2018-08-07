import { TestBed, inject } from '@angular/core/testing';

import { MysteryService } from './mystery.service';

describe('MysteryService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [MysteryService]
    });
  });

  it('should be created', inject([MysteryService], (service: MysteryService) => {
    expect(service).toBeTruthy();
  }));
});
