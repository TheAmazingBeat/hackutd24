import { Company } from './company';

export interface User {
  name: string;
  email: string;
  phone: string;
  username: string;
  password: string;
  preferences: {
    industries: string[];
    investmentType: 'Short-term' | 'Long-term' | '';
  };
  investments: Company[];
  newPerson: boolean;
  checkingAccount?: {
    accountNumber: number;
    balance: number;
    transactions: {
      date: Date;
      description: string;
      amount: number;
    }[];
  };
  savingsAccount?: {
    accountNumber: number;
    balance: number;
    transactions: {
      date: Date;
      description: string;
      amount: number;
    }[];
  };
}
