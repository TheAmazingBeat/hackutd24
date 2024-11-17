import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';

const routes: Routes = [
  {
    path: '',
    component: TabsPage,
    children: [
      {
        path: 'login',
        loadChildren: () =>
          import('../pages/login/login.module').then((m) => m.LoginPageModule),
      },
      {
        path: 'register',
        loadChildren: () =>
          import('../pages/register/register.module').then(
            (m) => m.RegisterPageModule
          ),
      },
      {
        path: 'for-you',
        loadChildren: () =>
          import('../tab1-for-you/tab1.module').then((m) => m.Tab1PageModule),
      },
      {
        path: 'portfolio',
        loadChildren: () =>
          import('../tab2-portfolio/tab2.module').then((m) => m.Tab2PageModule),
      },
      {
        path: 'accounts',
        loadChildren: () =>
          import('../tab3-accounts/tab3.module').then((m) => m.Tab3PageModule),
      },
      {
        path: 'profile',
        loadChildren: () =>
          import('../tab4-profile/tab4.module').then((m) => m.Tab4PageModule),
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
