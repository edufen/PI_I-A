**Documentação do Cartão de Vacinação**

O projeto do Cartão de Vacinação tem como objetivo fornecer uma plataforma para usuários acompanharem seu histórico de vacinação, além de permitir que administradores gerenciem o sistema, registrando pacientes, vacinas e administrando doses. Este projeto é uma iniciativa educacional e acadêmica, desenvolvida exclusivamente como parte de um trabalho acadêmico em uma instituição de ensino superior. Não possui fins lucrativos e não está destinado à comercialização. O objetivo principal é criar uma solução para acompanhamento do histórico de vacinação dos usuários e facilitar a administração do sistema de vacinação para os administradores, com foco no aprendizado e na aplicação prática dos conhecimentos adquiridos durante o curso universitário. 

**Funcionalidades**

*Para Usuários Registro e Log-in:*

Os usuários podem se cadastrar fornecendo informações como **nome, CPF, telefone, código SUS e senha**. Após o registro, podem fazer login para acessar as funcionalidades do sistema.

*Verificação de Dados:*

Os usuários podem checar suas informações cadastradas, exceto a senha. Podem também verificar o status de vacinação para uma vacina específica.

*Para Administradores Registro de Pacientes:*

Administradores têm a capacidade de registrar novos pacientes no sistema, fornecendo informações pessoais como nome, CPF, data de nascimento, telefone, código SUS e senha.

*Registro de Novas Vacinas no Sistema:*

Podem registrar novas vacinas no sistema, especificando **nome, doses tomadas e doses necessárias**.

*Aplicação de Vacinas:*

Os administradores podem aplicar vacinas a pacientes específicos, informando o CPF do paciente e o identificador da vacina. Após a aplicação bem-sucedida, o sistema exibirá a próxima dose, se aplicável.

*Verificação de Dados:*

É possível verificar e/ou modificar dados de paciente no sistema.

*Exportação de Dados:*

Há uma opção para exportar os dados de vacinas e pacientes para arquivos CSV.

**Utilização do Programa**

Ao executar o código, o usuário terá as seguintes opções:

**Digitar '1' para se registrar.**

Ao se registrar, o usuário precisará fornecer:

**Nome completo; CPF; Data de nascimento; Telefone; Código SUS; Senha;**

Após o registro, fazer login. É necessário informar **CPF e senha.**

Opção para fazer login como administrador. Não é possível cadastrar um usuário como administrador ao usar o programa, os usuários e senhas de admin já estão definidos dentro do código.

Opção para sair do programa.

Após o registro, o usuário pode fazer login, onde terá as seguintes opções:

**Logout; Checar informações cadastradas; Verificar status de vacinação;**

Ao fazer login como Administrador:

**Logout; Registrar Paciente; Registrar Vacina; Aplicar Vacina; Checar informações do paciente; Verificar status de Vacinação; Exportar Dados; Sair;**

**Sobre o Código**

Inicialmente, são importadas as bibliotecas necessárias para o funcionamento do código. A biblioteca **'csv'** é empregada para manipulação de arquivos CSV, enquanto a biblioteca **'datetime'** é utilizada para lidar com datas e horas em Python.

Em seguida, são definidas as constantes que representam os identificadores das vacinas presentes no sistema, uma vez que esses valores não serão alterados durante a execução do programa.

Posteriormente, são criadas classes para representar pacientes e vacinas, com o objetivo de estruturar os dados e operações relacionadas a essas entidades. Os dados referentes à utilização do programa são armazenados em dicionários. Ademais, são previamente definidos logins e senhas para administradores no respectivo dicionário.

Desenvolvem-se então as seguintes funções:

* Verificar se o paciente já está cadastrado no sistema.
* Verificar o status de vacinação.
* Cadastrar pacientes.
* Checar informações de um paciente específico.
* Realizar login como usuário
* Registrar vacinas.
* Aplicar vacinas.
* Realizar login como administrador.
* Exportar dados.

Na função principal do código, ao ser executado, é apresentada uma tela de interface para:

* Realização do registro de usuários.
* Login como usuário.
* Login como administrador.

Ao fazer login como usuário, é possível efetuar logout, checar informações ou verificar o status da vacinação. Já ao fazer login como administrador, é
