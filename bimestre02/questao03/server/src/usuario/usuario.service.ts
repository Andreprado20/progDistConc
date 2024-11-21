import { Injectable } from "@nestjs/common";
import { Prisma, usuario } from "@prisma/client";
import { PrismaService } from "src/prisma.service";

@Injectable()
export class usuarioServices {
  constructor(private prisma: PrismaService) { }

  async findusuario(id: Prisma.usuarioWhereUniqueInput): Promise<usuario | null> {
    return this.prisma.usuario.findUnique({
      where: id,
    });
  }

  async findAllProfesores(params: {
    skip?: number;
    take?: number;
    cursor?: Prisma.usuarioWhereUniqueInput;
    where?: Prisma.usuarioWhereInput;
    orderBy?: Prisma.usuarioOrderByWithRelationInput;
  }): Promise<usuario[]> {
    const { skip, take, cursor, where, orderBy } = params;
    return this.prisma.usuario.findMany({
      skip,
      take,
      cursor,
      where,
      orderBy,
    });
  }

  async createusuario(data: Prisma.usuarioCreateInput): Promise<usuario> {
    return this.prisma.usuario.create({
      data,
    });
  }

  async updateusuario(params: {
    id: Prisma.usuarioWhereUniqueInput;
    data: Prisma.usuarioUpdateInput;
  }): Promise<usuario> {
    const { id, data } = params;
    return this.prisma.usuario.update({
      where: id,
      data,
    })
  }

  async deleteusuario(id: Prisma.usuarioWhereUniqueInput): Promise<usuario> {
    return this.prisma.usuario.delete({
      where: id,
    })
  }
}
