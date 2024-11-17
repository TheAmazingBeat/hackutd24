import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-loan-details',
  templateUrl: './loan-details.component.html',
  styleUrls: ['./loan-details.component.scss'],
})
export class LoanDetailsComponent implements OnInit {
  @Input() amount!: number; // Loan amount input
  @Input() money!: number; // Asset value input
  @Input() credit_history!: number; // Credit history input

  apiResponse: string | null = null; // Store backend response
  loading: boolean = false; // Loading state

  constructor(private modalController: ModalController, private http: HttpClient) {}

  ngOnInit() {
    this.getLoanEvaluation();
  }

  // Fetch the loan evaluation from the backend API
  getLoanEvaluation() {
    this.loading = true; // Show loading spinner
    const apiUrl = 'http://localhost:5000/api/accounts'; // Replace with your backend URL
    const requestBody = {
      amount: this.amount,
      money: this.money,
      credit_history: this.credit_history,
    };

    this.http.post<{ response: string }>(apiUrl, requestBody).subscribe(
      (data) => {
        this.apiResponse = data.response; // Store API response
        this.loading = false; // Hide loading spinner
      },
      (error) => {
        console.error('API error:', error);
        this.apiResponse = 'An error occurred while processing your request.';
        this.loading = false; // Hide loading spinner
      }
    );
  }

  // Close the modal
  close() {
    this.modalController.dismiss();
  }
}
