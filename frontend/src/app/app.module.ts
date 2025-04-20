import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { ScenarioInputComponent } from './pages/scenario-input/scenario-input.component';
import { ResultsComponent } from './pages/results/results.component';
import { TypesOfNegotiationComponent } from './pages/types-of-negotiation/types-of-negotiation.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ScenarioInputComponent,
    ResultsComponent,
    TypesOfNegotiationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
