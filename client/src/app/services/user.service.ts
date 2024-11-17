import { Injectable } from '@angular/core';
import { User } from '../interfaces/user';

@Injectable({
  providedIn: 'root',
})
export class UserService {
  users: User[] = [];
  user: User | null = null;
  loggedIn = false;

  constructor() {}

  login(username: string, password: string) {
    this.users.forEach((user) => {
      if (user.username === username && user.password === password) {
        this.user = user;
        this.loggedIn = true;
      }
    });
  }

  logout() {
    this.user = null;
    this.loggedIn = false;
  }

  register(user: User) {
    this.users.push(user);
    this.user = user
  }

  updatePreferences(preference: {
    industries: string[];
    investmentType: 'Short-term' | 'Long-term' | '';
  }) {
    if (this.user) {
      this.user.preferences = preference;
    }
  }
}
