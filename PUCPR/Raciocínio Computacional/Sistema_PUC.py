print('-='*20)
print('''BEM VINDO AO SISTEMA PUC
      
Esse é um sistema CRUD, ou seja, um sistema para gestão de dados acadêmicos. 
Aqui poderemos fazer a gestão de dados de estudantes, disciplinas, professores, turmas e matrículas.
''')

print('''----- MENU PRINCIPAL -----
Selecione a opção desejada:
[ 1 ] Gerenciar Estudantes
[ 2 ] Gerenciar Professores
[ 3 ] Gerenciar Disciplinas
[ 4 ] Gerenciar Turmas
[ 5 ] Gerenciar Matrículas
[ 9 ] Sair / Finalizar
''')
print('-='*20)

resp_usuario = int(input('Informe a opção desejada: '))

if resp_usuario == 1 or resp_usuario == 'Gerenciar Estudantes':
    print('-='*20)
    print("[ESTUDANTES] Menu de Operações")
    print('-='*20)
    print('''Selecione a opção desejada:
    [ 1 ] Incluir.
    [ 2 ] Listar.
    [ 3 ] Atualizar.
    [ 4 ] Excluir.
    [ 9 ] Voltar ao menu principal.''')
elif resp_usuario == 2 or resp_usuario == 'Gerenciar Professores':
    print('-='*20)
    print("[PROFESSORES] Menu de Operações")
    print('-='*20)
    print('''Selecione a opção desejada:
    [ 1 ] Incluir.
    [ 2 ] Listar.
    [ 3 ] Atualizar.
    [ 4 ] Excluir.
    [ 9 ] Voltar ao menu principal.''')
elif resp_usuario == 3 or resp_usuario == 'Gerenciar Disciplinas':
    print('-='*20)
    print("[DISCIPLINAS] Menu de Operações")
    print('-='*20)
    print('''Selecione a opção desejada:
    [ 1 ] Incluir.
    [ 2 ] Listar.
    [ 3 ] Atualizar.
    [ 4 ] Excluir.
    [ 9 ] Voltar ao menu principal.''')
elif resp_usuario == 4 or resp_usuario == 'Gerenciar Turmas':
    print('-='*20)
    print("[TURMAS] Menu de Operações")
    print('-='*20)
    print('''Selecione a opção desejada:
    [ 1 ] Incluir.
    [ 2 ] Listar.
    [ 3 ] Atualizar.
    [ 4 ] Excluir.
    [ 9 ] Voltar ao menu principal.''')
elif resp_usuario == 5 or resp_usuario == 'Gerenciar Matrículas':
    print('-='*20)
    print("[MATRÍCULAS] Menu de Operações")
    print('-='*20)
    print('''Selecione a opção desejada:
    [ 1 ] Incluir.
    [ 2 ] Listar.
    [ 3 ] Atualizar.
    [ 4 ] Excluir.
    [ 9 ] Voltar ao menu principal.''')