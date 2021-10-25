CREATE DATABASE SISTEMA_FINANCEIRO 
GO
USE [SISTEMA_FINANCEIRO]
GO
/****** Object:  Table [dbo].[CONTA_EXTRATO]    Script Date: 17/10/2021 23:06:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CONTA_EXTRATO](
	[COD] [int] IDENTITY(1,1) NOT NULL,
	[NOME] [varchar](50) NOT NULL,
	[DESCRICAO] [varchar](250) NOT NULL,
	[AGENCIA] [varchar](20) NOT NULL,
	[NUMERO_CONTA] [varchar](25) NOT NULL,
	[SALDO_INICIAL] [decimal](18, 2) NOT NULL,
	[ATIVO] [bit] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PESSOA]    Script Date: 17/10/2021 23:06:22 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PESSOA](
	[COD] [int] IDENTITY(1,1) NOT NULL,
	[NOME] [varchar](100) NOT NULL,
	[ENDERECO] [varchar](250) NOT NULL,
	[CPF] [varchar](14) NOT NULL,
	[CNPJ] [varchar](18) NOT NULL,
	[CLIENTE] [bit] NOT NULL,
	[FORNECEDOR] [bit] NOT NULL,
	[FUNCIONARIO] [bit] NOT NULL,
	[LOGIN] [varchar](25) NOT NULL,
	[SENHA] [varchar](15) NOT NULL,
	[ATIVO] [bit] NOT NULL
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[CONTA_EXTRATO] ADD  CONSTRAINT [DF_CONTA_EXTRATO_NOME]  DEFAULT ('') FOR [NOME]
GO
ALTER TABLE [dbo].[CONTA_EXTRATO] ADD  CONSTRAINT [DF_CONTA_EXTRATO_DESCRICAO]  DEFAULT ('') FOR [DESCRICAO]
GO
ALTER TABLE [dbo].[CONTA_EXTRATO] ADD  CONSTRAINT [DF_CONTA_EXTRATO_AGENCIA]  DEFAULT ('') FOR [AGENCIA]
GO
ALTER TABLE [dbo].[CONTA_EXTRATO] ADD  CONSTRAINT [DF_CONTA_EXTRATO_NUMERO_CONTA]  DEFAULT ('') FOR [NUMERO_CONTA]
GO
ALTER TABLE [dbo].[CONTA_EXTRATO] ADD  CONSTRAINT [DF_CONTA_EXTRATO_SALDO_INICIAL]  DEFAULT ((0)) FOR [SALDO_INICIAL]
GO
ALTER TABLE [dbo].[CONTA_EXTRATO] ADD  CONSTRAINT [DF_Table_1_STATUS]  DEFAULT ((1)) FOR [ATIVO]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_NOME]  DEFAULT ('') FOR [NOME]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_Table_1_ENDEREÇO]  DEFAULT ('') FOR [ENDERECO]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_CPF]  DEFAULT ('') FOR [CPF]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_CNPJ]  DEFAULT ('') FOR [CNPJ]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_CLIENTE]  DEFAULT ((0)) FOR [CLIENTE]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_FORNECEDOR]  DEFAULT ((0)) FOR [FORNECEDOR]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_FUNCIONARIO]  DEFAULT ((0)) FOR [FUNCIONARIO]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_LOGIN]  DEFAULT ('') FOR [LOGIN]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_SENHA]  DEFAULT ('') FOR [SENHA]
GO
ALTER TABLE [dbo].[PESSOA] ADD  CONSTRAINT [DF_PESSOA_STATUS]  DEFAULT ((0)) FOR [ATIVO]
GO
------------- ******************* ---------------


ALTER TABLE PESSOA
ADD RAZAO_SOCIAL VARCHAR(60) NOT NULL DEFAULT ''
GO
ALTER TABLE PESSOA
ADD TELEFONE	 VARCHAR(30) NOT NULL DEFAULT ''
GO
ALTER TABLE PESSOA
ADD CELULAR VARCHAR(30) NOT NULL DEFAULT ''
GO
ALTER TABLE PESSOA
ADD EMAIL VARCHAR(255) NOT NULL DEFAULT ''
GO
ALTER TABLE PESSOA
ADD DATA_CADASTRO DATE NOT NULL DEFAULT (GETDATE())
GO