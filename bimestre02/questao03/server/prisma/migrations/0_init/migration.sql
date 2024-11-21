-- CreateTable
CREATE TABLE "aluno" (
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(60) NOT NULL,
    "curso" VARCHAR NOT NULL,
    "email" VARCHAR NOT NULL,
    "matricula" VARCHAR(9) NOT NULL,
    "grupo_id" INTEGER NOT NULL,

    CONSTRAINT "aluno_pk" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "avaliacao" (
    "id" INTEGER NOT NULL,
    "nota_avaliacao" REAL NOT NULL,
    "usuario_id" INTEGER NOT NULL,

    CONSTRAINT "avaliacao_pk" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "grupo" (
    "id" INTEGER NOT NULL,
    "nome_projeto" VARCHAR NOT NULL,

    CONSTRAINT "grupo_pk" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "usuario" (
    "id" INTEGER NOT NULL,
    "nome" VARCHAR(60) NOT NULL,
    "matricula" VARCHAR NOT NULL,
    "email" VARCHAR NOT NULL,

    CONSTRAINT "usuario_pk" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "projeto" (
    "id" INTEGER NOT NULL,
    "tema" VARCHAR NOT NULL,
    "estande" INTEGER NOT NULL,
    "grupo_id" INTEGER NOT NULL,
    "data_apresentacao" DATE NOT NULL,
    "avaliacao_id" INTEGER NOT NULL,

    CONSTRAINT "projeto_pk" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "aluno_idx" ON "aluno"("matricula");

-- CreateIndex
CREATE UNIQUE INDEX "usuario_idx" ON "usuario"("matricula");

-- AddForeignKey
ALTER TABLE "aluno" ADD CONSTRAINT "grupo_aluno_fk" FOREIGN KEY ("grupo_id") REFERENCES "grupo"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "avaliacao" ADD CONSTRAINT "usuario_avaliacao_fk" FOREIGN KEY ("usuario_id") REFERENCES "usuario"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "projeto" ADD CONSTRAINT "avaliacao_projeto_fk" FOREIGN KEY ("avaliacao_id") REFERENCES "avaliacao"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

-- AddForeignKey
ALTER TABLE "projeto" ADD CONSTRAINT "grupo_projeto_fk" FOREIGN KEY ("grupo_id") REFERENCES "grupo"("id") ON DELETE NO ACTION ON UPDATE NO ACTION;

