import { Component, Input, OnInit } from '@angular/core';
import { Company } from 'src/app/interfaces/company';

@Component({
  selector: 'app-invest-card',
  templateUrl: './invest-card.component.html',
  styleUrls: ['./invest-card.component.scss'],
})
export class InvestCardComponent {
  @Input() company: Company | null = null;

  constructor() {

  }
}
