import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { User } from '../interfaces/user';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  user: User | null = null;
  companies: any[] = [];
  private apiRoute = 'http://localhost:5000/';

  constructor(private httpClient: HttpClient) {}

  // async getUser(){
  //   this.user = await this.httpClient.get<User>('http://localhost:3000/user')
  // }

  initialize() {
    return this.httpClient.get(`${this.apiRoute}/fyp`);
  }
  api_intialize() {
    return this.httpClient.get(`${this.apiRoute}/api/accounts`);
  }

  get_fyp_openai() {
    return this.httpClient.get(`${this.apiRoute}/api/fyp`);
  }


  convertByteToImage(byteString: string) {
    return 'data:image/jpeg;base64,' + byteString;
  }
}
