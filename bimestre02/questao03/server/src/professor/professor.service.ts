import { Injectable } from "@nestjs/common";
import { Prisma, professor } from "@prisma/client";
import { PrismaService } from "src/prisma.service";

@Injectable()
export class professorServices {
  constructor(private prisma: PrismaService) { }

  async findProfessor(id: Prisma.professorWhereUniqueInput): Promise<professor | null> {
    return this.prisma.professor.findUnique({
      where: id,
    });
  }

  async findAllProfesores(params: {
    skip?: number;
    take?: number;
    cursor?: Prisma.professorWhereUniqueInput;
    where?: Prisma.professorWhereInput;
    orderBy?: Prisma.professorOrderByWithRelationInput;
  }): Promise<professor[]> {
    const { skip, take, cursor, where, orderBy } = params;
    return this.prisma.professor.findMany({
      skip, 
      take, 
      cursor, 
      where, 
      orderBy,
    });
  }

  async createProfessor(data: Prisma.professorCreateInput): Promise<professor> {
    return this.prisma.professor.create({
      data,
    });
  }

  async updateProfessor(params: {
    id: Prisma.professorWhereUniqueInput;
    data: Prisma.professorUpdateInput;
  }): Promise<professor>{
    const {id, data} = params;
    return this.prisma.professor.update({
      where: id,
      data,
    })
  }

  async deleteProfessor(id: Prisma.professorWhereUniqueInput):Promise<professor>{
    return this.prisma.professor.delete({
      where: id,
    })
  }
}
