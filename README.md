# Sistema de Gerenciamento do Cartão de Vacinas

## Introdução

Este sistema de gerenciamento de vacinas foi desenvolvido para facilitar o acompanhamento e a administração de vacinas, oferecendo soluções tanto para pacientes quanto para administradores. Com um cartão de vacinas virtual e funcionalidades de agendamento automático, o sistema busca proporcionar um controle mais eficiente e acessível para todos os envolvidos no processo de vacinação.

## Funcionalidades para Pacientes

### 1. Cadastro de Usuários

- **Cadastro:** Os pacientes podem se cadastrar fornecendo os seguintes dados:
  - Nome completo
  - CPF
  - Data de nascimento (DD/MM/AAAA)
  - Telefone (DDD + número com o dígito 9)
  - Código de Identificação do Cartão SUS
  - Senha

### 2. Acesso ao Cartão de Vacinas Virtual

- **Cartão Virtual:** Após o cadastro, os pacientes têm acesso ao seu cartão de vacinas virtual, onde podem visualizar e acompanhar suas vacinas.

### 3. Exibição de Informações e Acompanhamento de Vacinas

- **Informações Pessoais:** Os pacientes podem verificar suas informações pessoais e o status de vacinação.
- **Acompanhamento:** O sistema agenda automaticamente a próxima dose para 30 dias após a aplicação da vacina.

## Funcionalidades para Administradores

### 1. Acesso Completo

- **Acesso Total:** Os administradores têm acesso a todas as funcionalidades do sistema.

### 2. Registro de Nova Vacina

- **Adicionar Vacinas:** Capacidade de registrar novas vacinas, incluindo informações como nome, dose, lote, validade, fabricante e identificador.

### 3. Aplicação de Vacinas

- **Aplicar Vacinas:** Administradores podem aplicar vacinas aos pacientes cadastrados usando o CPF e o identificador da vacina. Caso a vacina tenha múltiplas doses, o sistema agenda automaticamente a próxima dose para 30 dias após a aplicação.

### 4. Exportação de Dados

- **Exportar Dados:** Possibilidade de exportar dados de pacientes e vacinas para um arquivo `.csv`, facilitando análises e organização interna.

## Considerações Finais

O sistema de gerenciamento de vacinas apresentado oferece uma solução abrangente para pacientes e administradores. Com funcionalidades como o cartão de vacinas virtual, agendamento automático e exportação de dados, o sistema visa simplificar o acompanhamento e a administração das vacinas, podendo ser adaptado conforme as necessidades específicas.

## Tutorial de Uso do Programa

### 1. Usuário Comum

1. **Registro:**
   - Selecione a opção `1` para realizar o registro.
   - Forneça as informações solicitadas: nome completo, CPF, data de nascimento (DD/MM/AAAA), telefone (DDD + número com o dígito 9), código do Cartão SUS e senha.
   - Após o registro, retorne ao menu principal digitando `2` para fazer login ou `0` para sair.

2. **Login:**
   - Digite o CPF e a senha cadastrada para acessar o sistema.
   - Após o login, você pode:
     - Digitar `1` para fazer logout.
     - Digitar `2` para verificar suas informações pessoais e o status de vacinação.
     - Digitar `3` para verificar o status de vacinação, incluindo vacinas tomadas, doses necessárias e data da próxima dose.

### 2. Usuário Administrador

1. **Logout e Acesso:**
   - Digite `1` para fazer logout.

2. **Cadastro e Administração:**
   - **Registrar Paciente:** Digite `2` para registrar um novo paciente. O sistema não permite cadastrar pacientes com CPF já existente.
   - **Registrar Vacina:** Digite `3` para registrar uma nova vacina. Forneça todas as informações necessárias, como nome, dose, lote, validade, fabricante e identificador.
   - **Aplicar Vacina:** Digite `4` para aplicar uma vacina a um paciente cadastrado. Utilize o CPF do paciente e o identificador da vacina. O sistema agenda automaticamente a próxima dose para 30 dias após a aplicação da primeira, se necessário.
   - **Informações do Paciente:** Digite `5` para verificar informações de um paciente usando o CPF como identificação.
   - **Status de Vacinação:** Digite `6` para verificar o status de vacinação de um paciente usando o CPF como identificação.
   - **Exportar Dados:** Digite `7` para exportar dados. Um arquivo `.csv` contendo informações dos pacientes e das vacinas será gerado para análise e organização interna.

**Observação:** Siga as instruções apresentadas pelo programa para garantir o correto funcionamento das operações.

## Assinatura

Desenvolvido por [Eduardo Lima](https://www.linkedin.com/in/eduardobdlima)  
Curso [Big Data e Inteligência Artificial](https://www.pucgoias.edu.br/cursos/graduacao/big-data-e-inteligencia-artificial-ead/) - Projeto Integrador I-A   
[PUC Goiás - Pontifícia Universidade Católica de Goiás](https://www.pucgoias.edu.br/)  
Abril de 2024
