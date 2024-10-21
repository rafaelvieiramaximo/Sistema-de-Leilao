import { NgModule } from '@angular/core';
import { ServerModule } from '@angular/platform-server';
import { HttpClientModule } from '@angular/common/http';
import { AppModule } from './app.module';
import { AppComponent } from './app.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';


@NgModule({
  imports: [
    AppModule,
    ServerModule,
    HttpClientModule, // Import HttpClientModule to make HTTP requests in Angular
    FontAwesomeModule, // Import FontAwesomeModule to use Font Awesome icons
  ],
  bootstrap: [AppComponent],
})
export class AppServerModule {}
