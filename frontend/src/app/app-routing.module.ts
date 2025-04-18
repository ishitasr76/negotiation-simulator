import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { ScenarioInputComponent } from './pages/scenario-input/scenario-input.component';
import { ResultsComponent } from './pages/results/results.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'input', component: ScenarioInputComponent },
  { path: 'results', component: ResultsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
