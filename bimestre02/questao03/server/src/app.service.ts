import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Seja Bem Vindo à nossa API de teste com NestJS';
  }
}
