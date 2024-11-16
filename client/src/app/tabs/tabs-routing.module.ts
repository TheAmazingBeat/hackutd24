import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';

const routes: Routes = [
  {
    path: '',
    component: TabsPage,
    children: [
      {
        path: 'for-you',
        loadChildren: () =>
          import('../tab1-for-you/tab1.module').then((m) => m.Tab1PageModule),
      },
      {
        path: 'accounts',
        loadChildren: () =>
          import('../tab2-accounts/tab2.module').then((m) => m.Tab2PageModule),
      },
      {
        path: 'profile',
        loadChildren: () =>
          import('../tab3-profile/tab3.module').then((m) => m.Tab3PageModule),
      },
      {
        path: '',
        redirectTo: '/for-you',
        pathMatch: 'full',
      },
    ],
  },
  {
    path: '',
    redirectTo: '/for-you',
    pathMatch: 'full',
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
})
export class TabsPageRoutingModule {}
