import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaService } from './prisma.service';
import { usuarioController } from './usuario/usuario.controller';
import { usuarioServices } from './usuario/usuario.service';

@Module({
  imports: [],
  controllers: [AppController, usuarioController],
  providers: [PrismaService, AppService, usuarioServices],
})
export class AppModule { }
