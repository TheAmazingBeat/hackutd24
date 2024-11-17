import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/interfaces/user';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage {
  username: string = ''
  password: string = ''

  constructor(private userService: UserService) { }

  registerUser(){
    const newUser: User = {
      name: 'John Doe',
      username: this.username,
      password: 'password',
      email: 'john.doe@email.com',
      phone: '123-456-7890',
      preferences: {
        industries: [],
        investmentType: '',
      },
      newPerson: true,
      investments: [],
    }

    this.userService.register(newUser)

    
  }
}
