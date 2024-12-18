import { IonicModule } from '@ionic/angular';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Tab1Page } from './tab1.page';

import { Tab1PageRoutingModule } from './tab1-routing.module';
import { InvestCardComponent } from './components/invest-card/invest-card.component';
import { InvestModalComponent } from './components/invest-modal/invest-modal.component';
import { SharedModule } from '../shared/shared.module';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    Tab1PageRoutingModule,
    SharedModule
  ],
  declarations: [Tab1Page, InvestCardComponent, InvestModalComponent],
})
export class Tab1PageModule {}
