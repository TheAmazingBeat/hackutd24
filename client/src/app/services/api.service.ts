import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../interfaces/user';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  user: User | null = null;


  constructor(private httpClient: HttpClient) { }

  // async getUser(){
  //   this.user = await this.httpClient.get<User>('http://localhost:3000/user')
  // }

  async getForYou(){
  }
}
