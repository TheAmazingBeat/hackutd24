import { Component, OnInit } from '@angular/core';
import { Company } from '../interfaces/company';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss'],
})
export class Tab1Page implements OnInit {
  recommendedCompanies: Company[] = [
    // {
    //   name: 'Company 1',
    //   description: 'Company 1 Description',
    //   industry: 'Industry 1',
    //   location: 'Location 1',
    //   salePrice: 100,
    //   priceChange: 10,
    //   trendImage: 'https://via.placeholder.com/150',
    // },
    // {
    //   name: 'Company 2',
    //   description: 'Company 2 Description',
    //   industry: 'Industry 2',
    //   location: 'Location 2',
    //   salePrice: 200,
    //   priceChange: -5,
    //   trendImage: 'https://via.placeholder.com/150',
    // },
    // {
    //   name: 'Company 3',
    //   description: 'Company 3 Description',
    //   industry: 'Industry 3',
    //   location: 'Location 3',
    //   salePrice: 300,
    //   priceChange: 0,
    //   trendImage: 'https://via.placeholder.com/150',
    // },
    // {
    //   name: 'Company 4',
    //   description: 'Company 4 Description',
    //   industry: 'Industry 4',
    //   location: 'Location 4',
    //   salePrice: 400,
    //   priceChange: 20,
    //   trendImage: 'https://via.placeholder.com/150',
    // },
  ];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.initialize().subscribe(
      (response: any) => {
        response.map((company: any) => {
          const newCompany: Company = {
            name: company.name,
            description: 'Company Description',
            industry: 'Technology',
            salePrice: 300,
            priceChange: 0,
            trendImage: 'https://via.placeholder.com/150',
          };
          this.recommendedCompanies.push(newCompany);
        });
        console.log(response);
      },
      (error: any) => {
        console.error(error);
      }
    );
    // await this.apiService.initialize();
    // this.recommendedCompanies = this.apiService.companies;
  }
}
