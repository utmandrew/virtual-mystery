import { TestBed, inject } from '@angular/core/testing';

import { ArtifactserviceService } from './artifactservice.service';

describe('ArtifactserviceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ArtifactserviceService]
    });
  });

  it('should be created', inject([ArtifactserviceService], (service: ArtifactserviceService) => {
    expect(service).toBeTruthy();
  }));
});
