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
  negotiationType: string = '';

  stakeholderRoles: string[] = [
    'Government',
    'NGO',
    'Industry',
    'Public',
    'Academic',
    'Environmentalist'
  ];

  stakeholders: {
    name: string;
    role: string;
    description: string;
  }[] = [];

  frameworks = [
    { name: 'Utilitarianism', selected: false },
    { name: 'Deontology', selected: false },
    { name: 'Virtue Ethics', selected: false },
    { name: 'Rawlsian Justice', selected: false },
    { name: 'Care Ethics', selected: false }
  ];

  constructor(private router: Router) {}

  addStakeholder() {
    this.stakeholders.push({
      name: '',
      role: '',
      description: ''
    });
  }

  removeStakeholder(index: number) {
    this.stakeholders.splice(index, 1);
  }
  showResults = false;
  onSubmit() {
    const inputData = {
      scenario: this.scenario.trim(),
      stakeholders: this.stakeholders,
      negotiationType: this.negotiationType,
      frameworks: this.frameworks.filter(f => f.selected).map(f => f.name)
    };

    localStorage.setItem('scenarioData', JSON.stringify(inputData));
    console.log('Saved scenario data:', inputData);
    // this.router.navigate(['/results']);
    this.showResults=true
  }
}
