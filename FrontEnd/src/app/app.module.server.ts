import { NgModule } from '@angular/core';
import { ServerModule } from '@angular/platform-server';
import { HttpClientModule } from '@angular/common/http';

import { AppModule } from './app.module';
import { AppComponent } from './app.component';

@NgModule({
  imports: [
    AppModule,
    ServerModule,
    HttpClientModule,  // Import HttpClientModule to make HTTP requests in Angular
  ],
  bootstrap: [AppComponent],
})
export class AppServerModule {}
