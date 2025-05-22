# WOD Tracker

**Versão:** 1.0  
**Autores:**  
- Bernardo Cavalcanti Carneiro Leão  
- Júlio Gusmão Samico  
- Luiz Eduardo de Araújo Mariz  
- Pedro Xavier Gama Tenório Canel  

## 📌 Sobre o Sistema

O **WOD Tracker** é uma ferramenta interativa em Python voltada para praticantes de **CrossFit**, permitindo registrar, pesquisar e analisar treinos e metas.

---

## ⚙️ Como Executar o Sistema

1. Certifique-se de ter o **Python 3.8 ou superior** instalado.
2. Coloque os arquivos `projeto_fp.py` e `funcoes_projeto_fp.py` na **mesma pasta**.
3. Abra o **terminal** e navegue até essa pasta.
4. Execute o programa com o comando:
   ```bash
   python projeto_fp.py
   ```

---

## 📋 Menu Principal

Ao iniciar, o sistema exibe as seguintes opções:

```
1 - Criar o treino  
2 - Visualizar  
3 - Editar  
4 - Excluir  
5 - Filtrar  
6 - Adição de metas  
7 - Visualizar metas / atualizar  
8 - Adicionar algo  
9 - Nivelamento  
0 - Sair
```

---

## 🔍 Funcionalidades Detalhadas

### 1. Criar o Treino
- Insere um novo treino com:
  - Tipo de treino
  - Data de início
  - Duração (minutos)
  - Exercícios e repetições
- Salvo em `treino.txt`
- Mensagens de erro:
  - Entrada inválida para quantidade de exercícios
  - Erros inesperados

---

### 2. Visualizar
- Exibe o conteúdo de `treino.txt`
- Mensagens de erro:
  - Arquivo não encontrado
  - Erros inesperados

---

### 3. Editar
- Permite editar um treino existente:
  - Informar nome do treino
  - Confirmar edição
  - Inserir novo conteúdo
- Mensagens de erro:
  - Quantidade de exercícios inválida
  - Treino não encontrado
  - Arquivo não encontrado
  - Erros inesperados

---

### 4. Excluir
- Exclui treinos com base em um termo informado
- Confirmação exigida
- Mensagens de erro:
  - Nenhum treino encontrado
  - Arquivo não encontrado
  - Erros inesperados

---

### 5. Filtrar
- Busca por termo (ex: AMRAP) em `treino.txt`
- Mensagens de erro:
  - Nenhum treino encontrado
  - Arquivo não encontrado
  - Erros inesperados

---

### 6. Adição de Metas
- Adiciona metas com descrição
- Salvo em `metas.txt` (status inicial: inconcluído)
- Mensagens de erro:
  - Quantidade inválida de metas
  - Erro ao criar/acessar arquivo
  - Erros inesperados

---

### 7. Visualizar Metas / Atualizar
- Exibe metas de `metas.txt`
- Permite marcar metas como concluídas
- Mensagens de erro:
  - Arquivo não encontrado
  - Número de meta inválido
  - Número fora do intervalo
  - Erros inesperados

---

### 8. Adicionar Algo
- Adiciona conteúdo livre ao final de `treino.txt`
- Mensagens de erro:
  - Erros de escrita ou abertura

---

### 9. Nivelamento
- Avalia progresso baseado nas metas concluídas
- Classificação:
  - ≥ 80%: **Avançado**
  - 50%–79%: **Bom**
  - 20%–49%: **Baixo**
  - < 20%: **Melhore!**
- Mensagens de erro:
  - Arquivo `metas.txt` não encontrado
  - Erros inesperados
- ⚠️ O sistema subtrai 1 da contagem total para evitar erros com linhas em branco no final do arquivo

---

## 🎲 Sugestão de WOD Aleatório

Ao final da execução, o sistema sugere um dos **três treinos alternativos** de forma aleatória.

---

## ⚠️ Cuidados e Restrições

- Dados armazenados localmente em arquivos `.txt`
- Faça backups de `treino.txt` e `metas.txt`
- Evite edições manuais dos arquivos
- Insira dados válidos e consistentes
- Funciona apenas via **terminal (sem interface gráfica)**

---

## ✅ Requisitos

- Python 3.8+
- Terminal / Prompt de Comando
