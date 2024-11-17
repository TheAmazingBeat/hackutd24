import { Component } from '@angular/core';
import { Company } from '../interfaces/company';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss'],
})
export class Tab2Page {
  investments: Company[] = [
    {
      name: 'Apple',
      salePrice: 200,
      quantity: 1,
      priceChange: 0.5,
      description:
        'Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer software, and online services.',
      industry: 'Technology',
      trendImage: 'https://via.placeholder.com/150',
    },
    {
      name: 'Tesla',
      salePrice: 600,
      quantity: 1,
      priceChange: 1.5,
      description:
        'Tesla, Inc. is an American electric vehicle and clean energy company based in Palo Alto, California.',
      industry: 'Automotive',
      trendImage: 'https://via.placeholder.com/150',
    },
    {
      name: 'Amazon',
      salePrice: 3000,
      quantity: 1,
      priceChange: 2.5,
      description:
        'Amazon.com, Inc. is an American multinational technology company which focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence.',
      industry: 'Technology',
      trendImage: 'https:/via.placeholder.com/150',
    },
  ];

  constructor() {}
}
