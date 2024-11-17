export interface Company {
  name: string;
  description: string;
  industry: string;
  trendImage: string;
  salePrice: number;
  priceChange: number;
  location?: string;
  quantity?: number;
}
