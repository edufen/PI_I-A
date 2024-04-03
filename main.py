# A biblioteca datetime é usada para trabalhar com datas e horas 
from datetime import datetime, timedelta 
# A biblioteca csv é usada para trabalhar com arquivos CSV
import csv 

# Constantes para os identificadores de vacina
# Resolvi usar constantes para facilitar a leitura do código e também por serem valores que não devem ser alterados
CORONAVAC_ID = '123'
ASTRAZENECA_ID = '456'
PFIZER_ID = '789'

# Classe Paciente para representar um paciente
class Paciente:
    def __init__(self, nome, cpf, nascimento, telefone, codigo_sus, senha):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.telefone = telefone
        self.codigo_sus = codigo_sus
        self.senha = senha
        self.vacinas = {}
    # Método para adicionar uma vacina ao paciente
    def adicionar_vacina(self, identificador):
        if identificador not in self.vacinas:
            self.vacinas[identificador] = []
        self.vacinas[identificador].append(datetime.now())

# Classe Vacina para representar uma vacina
class Vacina:
    def __init__(self, nome, doses, lote, validade, fabricante, identificador): # O uso do self. é para referenciar a variável da classe
        self.nome = nome 
        self.doses = doses
        self.lote = lote
        self.validade = validade
        self.fabricante = fabricante
        self.identificador = identificador

# Dicionário para armazenar os pacientes, vacinas e administradores
pacientes = {} 
vacinas = {
    CORONAVAC_ID: Vacina('Coronavac', 3, 'Lote1', '31/12/2023', 'Sinovac', CORONAVAC_ID),
    ASTRAZENECA_ID: Vacina('AstraZeneca', 3, 'Lote2', '31/12/2023', 'Oxford', ASTRAZENECA_ID),
    PFIZER_ID: Vacina('Pfizer', 2, 'Lote3', '31/12/2023', 'Pfizer', PFIZER_ID),
}
administradores = {'admin': '123'}

# Função para verificar se o paciente já se encontra cadastrado no sistema, para impedir o cadastro de dois pacientes com o mesmo cpf
def paciente_existe(cpf):
    return cpf in pacientes

# Função para verificar o status de vacinação de um paciente
def verificar_status_vacinacao(cpf):
    if not paciente_existe(cpf): # Verifica se o paciente existe no sistema
        print('Paciente não encontrado.')
        return
    paciente = pacientes[cpf]
    for identificador, datas in paciente.vacinas.items():
        vacina = vacinas[identificador]
        print('Nome da vacina:', vacina.nome)
        print('Doses tomadas:', len(datas))
        print('Doses necessárias:', vacina.doses)
        if len(datas) < vacina.doses:
            print('Próxima dose:', datas[-1] + timedelta(days=30))

# Função para cadastrar um paciente
def cadastrar_paciente():
    nome = input('Digite o nome completo do paciente: ')
    cpf = input('Digite o CPF do paciente: ')
    if cpf in pacientes:
        print('Já existe um paciente cadastrado com este CPF.')
        return
    nascimento = input('Digite a data de nascimento do paciente (dd/mm/aaaa): ')
    try: # Verifica se a data de nascimento é válida
        datetime.strptime(nascimento, '%d/%m/%Y') 
    except ValueError:
        print('Data de nascimento inválida.')
        return
    telefone = input('Digite o telefone do paciente: ')
    codigo_sus = input('Digite o código do cartão SUS do paciente: ')
    senha = input('Digite a senha: ')
    pacientes[cpf] = Paciente(nome, cpf, nascimento, telefone, codigo_sus, senha)
    print('Paciente cadastrado com sucesso!')

# Função para checar as informações de um paciente
def checar_informacoes(cpf=None):
    if not cpf:
        cpf = input('Digite o CPF do paciente: ')
    if cpf in pacientes:
        paciente = pacientes[cpf]
        print(f'Nome: {paciente.nome}')
        print(f'CPF: {paciente.cpf}')
        print(f'Data de nascimento: {paciente.nascimento}')
        print(f'Telefone: {paciente.telefone}')
        print(f'Código SUS: {paciente.codigo_sus}')
        print('Vacinas:')
        for identificador, datas in paciente.vacinas.items():
            vacina = vacinas[identificador]
            print(f'  - {vacina.nome}: {len(datas)} dose(s)')
            if len(datas) < vacina.doses:
                proxima_dose = datas[-1] + timedelta(days=30)
                print('    Próxima dose:', proxima_dose.strftime('%d/%m/%Y'))  
    else:
        print('Paciente não encontrado.')
        
# Função para fazer login como paciente, já que ele não terá acesso a todas as funções do sistema
def login_paciente():
    cpf = input('Digite o CPF: ')
    senha = input('Digite a senha: ')
    if cpf in pacientes and pacientes[cpf].senha == senha:
        print('Seja bem-vindo ao cartão de vacinas virtual.')
        return cpf
    else:
        print('CPF ou senha incorretos.')
        return None

# Função para registrar uma vacina no sistema. nome/doses/lote/validade/fabricante/identificador
def registrar_vacina():
    nome = input('Digite o nome da vacina: ')
    doses = int(input('Digite a quantidade de doses necessárias: '))
    lote = input('Digite o lote da vacina: ')
    validade = input('Digite a data de validade da vacina (dd/mm/aaaa): ')
    fabricante = input('Digite o fabricante da vacina: ')
    identificador = input('Digite o identificador interno da vacina: ')
    if identificador in vacinas:
        print('Já existe uma vacina cadastrada com este identificador.')
        return
    vacinas[identificador] = Vacina(nome, doses, lote, validade, fabricante, identificador)
    print('Vacina registrada com sucesso!')

# Função para aplicar uma vacina em um paciente
def aplicar_vacina():
    cpf = input('Digite o CPF do paciente: ')
    identificador = input('Digite o identificador da vacina: ')
    if not paciente_existe(cpf):
        print('Paciente não encontrado.')
        return
    if identificador not in vacinas:
        print('Identificador de vacina não encontrado.')
        return
    paciente = pacientes[cpf]
    paciente.adicionar_vacina(identificador)
    print('Vacina aplicada com sucesso. A próxima dose será:', (datetime.now() + timedelta(days=30)).strftime('%d-%m-%y')) # Adicionei o strftime para formatar a data

# Função para fazer login como administrador, onde terá acesso a todas as funções do sistema
def login_admin():
    usuario = input('Digite o usuário: ')
    senha = input('Digite a senha: ')
    if usuario in administradores and administradores[usuario] == senha:
        print('Seja bem-vindo ao cartão de vacinas virtual.')
        return usuario
    else:
        print('Usuário ou senha incorretos.')
        return None

# Função para exportar os dados dos pacientes e vacinas para arquivos CSV
def exportar_dados():
    with open('pacientes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "CPF", "Nascimento", "Telefone", "Código SUS", "Vacinas"])
        for paciente in pacientes.values():
            vacinas_paciente = ', '.join([f'{vacinas[identificador].nome}: {len(datas)} dose(s)' for identificador, datas in paciente.vacinas.items()])
            writer.writerow([paciente.nome, paciente.cpf, paciente.nascimento, paciente.telefone, paciente.codigo_sus, vacinas_paciente])
    with open('vacinas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Doses", "Lote", "Validade", "Fabricante", "Identificador"])
        for vacina in vacinas.values():
            writer.writerow([vacina.nome, vacina.doses, vacina.lote, vacina.validade, vacina.fabricante, vacina.identificador])
    print('Dados exportados com sucesso!')

# Função principal do sistema
def main():
    usuario_logado = None
    tipo_usuario = None
    while True:
        if usuario_logado:
            print('1 - Logout')
            if tipo_usuario == 'paciente':
                print('2 - Checar as informações')
                print('3 - Verificar status de vacinação')
            elif tipo_usuario == 'admin':
                print('2 - Registrar paciente')
                print('3 - Registrar vacina')
                print('4 - Aplicar vacina')
                print('5 - Checar informações do paciente')
                print('6 - Verificar status de vacinação')
                print('7 - Exportar dados')
        else:
            print('1 - Registrar-se')
            print('2 - Fazer login como paciente')
            print('3 - Fazer login como administrador')
            print('0 - Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            if usuario_logado:
                usuario_logado = None
                tipo_usuario = None
            else:
                cadastrar_paciente()
        elif opcao == '2':
            if usuario_logado:
                if tipo_usuario == 'paciente':
                    checar_informacoes(usuario_logado)
                elif tipo_usuario == 'admin':
                    cadastrar_paciente()
            else:
                usuario_logado = login_paciente()
                if usuario_logado:
                    tipo_usuario = 'paciente'
        elif opcao == '3':
            if usuario_logado:
                if tipo_usuario == 'paciente':
                    verificar_status_vacinacao(usuario_logado)
                elif tipo_usuario == 'admin':
                    registrar_vacina()
            else:
                usuario_logado = login_admin()
                if usuario_logado:
                    tipo_usuario = 'admin'
        elif opcao == '4' and usuario_logado and tipo_usuario == 'admin':
            aplicar_vacina()
        elif opcao == '5' and usuario_logado and tipo_usuario == 'admin':
            cpf = input('Digite o CPF do paciente: ')
            checar_informacoes(cpf)
        elif opcao == '6' and usuario_logado and tipo_usuario == 'admin':
            cpf = input('Digite o CPF do paciente: ')
            verificar_status_vacinacao(cpf)
        elif opcao == '7' and usuario_logado and tipo_usuario == 'admin':
            exportar_dados()
        elif opcao == '0':
            break

if __name__ == '__main__':
    main()