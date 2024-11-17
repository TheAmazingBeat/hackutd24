import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { Company } from 'src/app/interfaces/company';

@Component({
  selector: 'app-invest-modal',
  templateUrl: './invest-modal.component.html',
  styleUrls: ['./invest-modal.component.scss'],
})
export class InvestModalComponent {
  @Input() company: Company | null = null;

  constructor(private modalController: ModalController) {}

  close() {
    this.modalController.dismiss();
  }
}
