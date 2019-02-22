import { TestBed, inject } from '@angular/core/testing';

import { ArtifactserviceService } from './artifactservice.service';
import { HttpClientModule } from '@angular/common/http';

describe('ArtifactserviceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ArtifactserviceService],
      imports: [
      HttpClientModule,
      ]
    });
  });

  it('should be created', inject([ArtifactserviceService], (service: ArtifactserviceService) => {
    expect(service).toBeTruthy();
  }));
});
