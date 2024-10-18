import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MyServiceService {

    private url = 'http://localhost:5000';

  constructor(private http: HttpClient) { }

  getProutos(): Observable<any> {
    return this.http.get(`${this.url}/produtos`);
  }

  addProdutos(item: any): Observable<any> {
    return this.http.post(`${this.url}/item`, item);
  }
  

  
}
