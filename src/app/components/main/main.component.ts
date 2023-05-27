import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
interface Message {
  from: string;
  text: string;
}
@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent {
  messages: Message[] = [];
  userInput = '';

  constructor(private http: HttpClient) { }

  sendMessage() {
    const userMessage: Message = {
      from: 'You',
      text: this.userInput
    };

    this.messages.push(userMessage);

    this.http.get<any>('http://localhost:5000/question?q=' + userMessage.text)
      .subscribe(response => {
        console.log(response);
        const botMessage: Message = {
          from: 'Bang',
          text: response
        };
        this.messages.push(botMessage);
      });
  }

  setInput(event: any) {
    this.userInput = event.target.value;
  }
}
