import { Body, Controller, Get, Param, Post, Put, Delete } from '@nestjs/common';
import { ApiTags } from '@nestjs/swagger'
import { usuarioServices } from './usuario.service';
import { usuario as usuarioModel } from '@prisma/client'
import { PrismaService } from '../prisma.service';

@Controller()
@ApiTags('prisma')
export class usuarioController {
  constructor(private readonly prismaService: PrismaService, private readonly usuarioService: usuarioServices) { }

  @Get('usuario/:id')
  async getusuarioById(@Param('id') id: string): Promise<usuarioModel> {
    return this.prismaService.usuario.findUnique({
      where: { id: +id },
    });
  }

  @Get('usuarios')
  async getAllusuarioes(): Promise<usuarioModel[]> {
    return this.prismaService.usuario.findMany();
  }

  @Post('usuario/post_usuario')
  async postusuario(
    @Body() postData: { id: number, nome: string, login: string, senha: string },
  ): Promise<usuarioModel> {
    const { id, nome, login, senha } = postData;
    return this.prismaService.usuario.create({
      data: { id, nome, login, senha }
    })
  }

  @Put('usuario/update/:id')
  async updateusuario(@Param('id') id: string, @Body() putData: { nome: string, login: string, senha: string}): Promise<usuarioModel> {
    const { nome, login, senha } = putData;
    return this.usuarioService.updateusuario({
      id: { id: Number(id) },
      data: { nome, login, senha }
    })
  }

  @Delete('usuario/delete/:id')
  async deleteusuario(@Param('id') id: string): Promise<usuarioModel> {
    return this.usuarioService.deleteusuario(
      { id: Number(id) },
    )
  }
}