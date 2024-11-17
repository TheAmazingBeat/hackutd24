import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { isPlatform } from '@ionic/angular';

const routes: Routes = [
  {
    path: '',
    loadChildren: () =>
      import('./tabs/tabs.module').then((m) => m.TabsPageModule),
    // loadChildren: () =>
    //   isPlatform('ios') || isPlatform('android')
    //     ? import('./tabs/tabs.module').then((m) => m.TabsPageModule)
    //     : import('./sidemenu/sidemenu.module').then(
    //         (m) => m.SidemenuPageModule
    //       ),
  },
];
@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules }),
  ],
  exports: [RouterModule],
})
export class AppRoutingModule {}
