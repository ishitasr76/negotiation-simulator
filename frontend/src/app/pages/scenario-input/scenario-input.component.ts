import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-scenario-input',
  templateUrl: './scenario-input.component.html',
  standalone: false,
  styleUrls: ['./scenario-input.component.css']
})
export class ScenarioInputComponent {
  scenario: string = '';

  constructor(private router: Router) {}

  onSubmit(): void {
    localStorage.setItem('scenario', this.scenario);
    // In the future: this.router.navigate(['/results']);
    console.log('Scenario saved:', this.scenario);
  }
}
