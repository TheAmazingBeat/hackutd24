import { Component } from '@angular/core';

@Component({
  selector: 'app-tab4',
  templateUrl: 'tab4.page.html',
  styleUrls: ['tab4.page.scss'],
})
export class Tab4Page {
  user = {
    name: 'John Doe',
    email: 'john.doe@email.com',
    phone: '123-456-7890',
    username: 'johndoe',
    password: 'password',
    preferences: {
      industries: ['Technology', 'Healthcare'],
      investmentType: 'Short-term',
    },
  };

  constructor() {}
}
