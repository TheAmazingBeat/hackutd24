import { Component } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { LoanDetailsComponent } from './loan-details/loan-details.component';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss'],
})
export class Tab3Page {
  constructor(
    private modalController: ModalController,
    private apiService: ApiService
  ) {}
  creditHistoryValue: number | null = null;

  async openLoanDetails(loan_amount: number, asset: number,credit_history: number) {
    console.log('Opening loan details modal');
    const modal = await this.modalController.create({
      component: LoanDetailsComponent,
      componentProps: {
        amount: loan_amount,
        money: asset,
        credit_history: credit_history  
      },
    });
   

    await modal.present();

  }


}
