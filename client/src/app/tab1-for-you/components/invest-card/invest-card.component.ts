import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { Company } from 'src/app/interfaces/company';
import { InvestModalComponent } from '../invest-modal/invest-modal.component';

@Component({
  selector: 'app-invest-card',
  templateUrl: './invest-card.component.html',
  styleUrls: ['./invest-card.component.scss'],
})
export class InvestCardComponent {
  @Input() company: Company | null = null;

  constructor(private modalController: ModalController) {}

  async openModal(company: Company) {
    // Open a modal with the company details
    const modal = await this.modalController.create({
      component: InvestModalComponent,
      componentProps: {
        company,
      },
    });

    modal.present();

    const { data } = await modal.onDidDismiss();
  }
}
