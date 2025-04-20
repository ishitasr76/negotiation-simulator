import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TypesOfNegotiationComponent } from './types-of-negotiation.component';

describe('TypesOfNegotiationComponent', () => {
  let component: TypesOfNegotiationComponent;
  let fixture: ComponentFixture<TypesOfNegotiationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [TypesOfNegotiationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TypesOfNegotiationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
