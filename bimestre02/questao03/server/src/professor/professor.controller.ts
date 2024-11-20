import { Body, Controller, Get, Param, Post, Put, Delete} from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger'
import { professorServices } from './professor.service';
import { professor as professorModel } from '@prisma/client'
import { PrismaService } from '../prisma.service';

@Controller()
@ApiTags('prisma')
export class ProfessorController {
  constructor(private readonly prismaService: PrismaService, private readonly professorService: professorServices) { }

  @Get('professor/:id')
  async getProfessorById(@Param('id') id: string): Promise<professorModel> {
    return this.prismaService.professor.findUnique({
      where: { id: +id },
    });
  }

  @Get('professores')
  async getAllProfessores(): Promise<professorModel[]> {
    return this.prismaService.professor.findMany();
  }

  @Post('professor/postProfessor')
  async postProfessor(
    @Body() postData: { id: number, nome: string, matricula: string, email: string },
  ): Promise<professorModel> {
    const { id, nome, matricula, email } = postData;
    return this.prismaService.professor.create({
      data: { id, nome, matricula, email }
    })
  }

  @Put('professor/update/:id')
  async updateProfessor(@Param('id') id: string, @Body() putData: { nome: string, matricula: string, email: string }): Promise<professorModel> {
    const { nome, matricula, email } = putData; 
    return this.professorService.updateProfessor({
      id: {id: Number(id)},
      data: {nome, matricula, email}
    })
  }

  @Delete('professor/delete/:id')
  async deleteProfessor(@Param('id') id: string): Promise<professorModel> {
    return this.professorService.deleteProfessor(
      {id: Number(id)},
    )
  }

}