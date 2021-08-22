import PySimpleGUI as sg
import random

class PassGen:
    def __init__(self):
        sg.theme('LightGray1')
        layout = [
            [sg.Text('SITE/SOFTWARE/JOGO', size=(20, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-MAIL/USUARIO', size=(20, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('TAMANHO DA SENHA', size=(20, 1)),
             sg.Combo(list(range(7, 16)), key='total_chars', default_value=7, size=(3, 1))],
            [sg.Button('GERAR')],
            [sg.Output(size=(45, 5))]
        ]
        self.janela = sg.Window('Gerador de senhas (Armazena no arquivo)', layout)

    def gerar_senha(self, valores):
        char_MAI = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        char_MIN = 'abcdefghijklmnopqrstuvwxyz'
        char_num = '1234567890'
        char_esp = '!@#$%¨&*'
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%¨&*'

        total = int(valores['total_chars'])
        temp = random.choices(char_MAI, k=1)
        temp.extend(random.choices(char_MIN, k=1))
        temp.extend(random.choices(char_num, k=1))
        temp.extend(random.choices(char_esp, k=1))
        temp2 = random.choices(char_list, k=total - len(temp))
        senha_list = temp + temp2
        new_pass = ''.join(senha_list)

        return new_pass

    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write(f'\nSite: {valores["site"]}, Usuário: {valores["usuario"]}, Senha: {nova_senha}')
        print('SENHA SALVA! ESTARÁ NO ARQUIVO senhas.txt.')

    def iniciar(self):
        while True:
            event, values = self.janela.read()

            if event == sg.WINDOW_CLOSED:
                break
            if event == 'GERAR':
                nova_senha = self.gerar_senha(values)
                print(nova_senha)
                self.salvar_senha(nova_senha, values)

def main():
    gerador = PassGen()
    gerador.iniciar()

if __name__ == '__main__':
    main()
