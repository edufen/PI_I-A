**Sistema do Gerenciamento do Cartão de Vacinas:**
**Funcionalidades para Pacientes e Administradores**

**1. Introdução**
O presente trabalho apresenta um sistema de gerenciamento de vacinas, destinado tanto aos pacientes quanto aos administradores. O sistema permite o cadastro de pacientes, fornecendo um cartão de vacinas virtual, além de oferecer funcionalidades como o acompanhamento de doses e agendamento automático de vacinas múltiplas. Para os administradores, há a possibilidade de registrar novas vacinas, aplicá-las aos pacientes e exportar dados para análises.

**2. Funcionalidades para Pacientes**
**2.1 Cadastro de Usuários:**
- Os pacientes podem se cadastrar no sistema fornecendo dados pessoais.
- É necessário criar uma senha durante o cadastro para posterior login.

**2.2 Acesso ao Cartão de Vacinas Virtual:**
- Após o cadastro, os pacientes têm acesso ao seu cartão de vacinas virtual.

**2.3 Exibição de Informações e Acompanhamento de Vacinas:**
- Os pacientes podem visualizar suas informações pessoais.
- Os pacientes podem acompanhar as próximas doses de vacinas aplicadas.
- O sistema agenda automaticamente a próxima dose para 30 dias após a aplicação.

**3. Funcionalidades para Administradores**
**3.1 Acesso Completo:**
- Os administradores possuem acesso a todas as funcionalidades do programa.

**3.2 Registro de Nova Vacina:**
- Capacidade de registrar novas vacinas no sistema.

**3.3 Aplicação de Vacinas:**
- Os administradores podem aplicar vacinas aos pacientes cadastrados, utilizando o CPF como identificação.

**3.4 Exportação de Dados:**
- Possibilidade de exportar dados de pacientes e vacinas para um arquivo “.csv”. Onde os dados exportados podem ser utilizados para análises ou organização interna.

**4. Considerações Finais**
O sistema de gerenciamento de vacinas apresentado oferece uma solução abrangente tanto para pacientes quanto para administradores. Com funcionalidades como o cartão de vacinas virtual, agendamento automático e exportação de dados, visa facilitar o acompanhamento e a administração das vacinas. A flexibilidade do sistema permite adaptações conforme as necessidades específicas de cada contexto de uso.

-----------------------------------------------------------------------

**Tutorial de Uso do Programa:**

**1. Usuário Comum:**

Ao inicializar o programa, selecione a opção "1" para realizar o registro.

Durante o registro, siga as instruções fornecidas pelo programa, fornecendo as seguintes informações:

Nome completo;
CPF;
Data de nascimento no formato (DD/MM/AAAA);
Telefone no formato DDD + número com o dígito 9;
Código de Identificação do Cartão SUS;
Senha;

Após o registro, retorne ao menu principal digitando "2" para fazer login ou "0" para sair.

Para fazer login, informe o CPF e a senha cadastrada para acessar o sistema.

Uma vez logado no sistema, você pode:

Digitar "1" para fazer logout
Digitar "2" para verificar suas informações, incluindo o status de vacinação caso tenha recebido alguma vacina
Digitar "3" para verificar o status de vacinação, mostrando as vacinas tomadas, doses necessárias e data da próxima dose.


**2. Usuário Administrador:**

Digite "1" para fazer logout.

Digite "2" para registrar um novo paciente. É importante observar que não é possível cadastrar um paciente cujo CPF já esteja no sistema, devido à validação do CPF implementada no código.

Digite "3" para registrar uma nova vacina. É necessário fornecer todas as informações solicitadas, incluindo nome, dose, lote, validade, fabricante e identificador.

Digite "4" para aplicar uma vacina a um paciente cadastrado no sistema. Você pode aplicar a vacina diretamente utilizando o CPF do paciente e o identificador da vacina. Caso a vacina tenha mais de uma dose, o sistema agendará automaticamente a próxima dose para 30 dias após a aplicação da primeira.

Digite "5" para verificar informações de um paciente utilizando o CPF como identificação.

Digite "6" para verificar o status de vacinação de um paciente utilizando o CPF como identificação.

Digite "7" para exportar dados. Será gerado um arquivo .csv contendo informações dos pacientes e das vacinas cadastradas no sistema.

Observação: Certifique-se de seguir as instruções do programa conforme apresentadas para garantir o correto funcionamento das operações.
