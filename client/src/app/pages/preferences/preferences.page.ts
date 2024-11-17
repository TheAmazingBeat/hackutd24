import { Component, OnInit } from '@angular/core';
import { UserService } from 'src/app/services/user.service';

@Component({
  selector: 'app-preferences',
  templateUrl: './preferences.page.html',
  styleUrls: ['./preferences.page.scss'],
})
export class PreferencesPage {
  preferredindustries: string[] = [];
  public progress = 0;
  riskType: 'Short-term' | 'Long-term' | '' = '';
  industries: string[] = [
    'Technology',
    'Healthcare',
    'Finance',
    'Real Estate',
    'Consumer Goods',
    'Energy',
    'Utilities',
    'Telecommunications',
    'Materials',
    'Industrials',
    'Consumer Services',
  ];

  constructor(private userService: UserService) {}

  nextStep() {
    this.progress += 50;
    this.userService.updatePreferences({
      industries: this.preferredindustries,
      investmentType: this.riskType,
    })

  }

  addIndustry(industry: string) {
    this.preferredindustries.push(industry);
  }

  toggleIndustry(industry: string) {
    const index = this.preferredindustries.indexOf(industry);
    if (index === -1) {
      this.preferredindustries.push(industry);
    } else {
      this.preferredindustries.splice(index, 1);
    }
  }

  isIndustrySelected(industry: string): boolean {
    return this.preferredindustries.includes(industry);
  }

  getChipColor(industry: string): string {
    return this.isIndustrySelected(industry) ? 'success' : 'secondary';
  }

  setRiskType(riskType: 'Short-term' | 'Long-term') {
    this.riskType = riskType;
  }
}
