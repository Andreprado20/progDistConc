import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PrismaService } from './prisma.service';
import { ProfessorController } from './professor/professor.controller';
import { professorServices } from './professor/professor.service';

@Module({
  imports: [],
  controllers: [AppController, ProfessorController],
  providers: [PrismaService, AppService, professorServices],
})
export class AppModule { }
