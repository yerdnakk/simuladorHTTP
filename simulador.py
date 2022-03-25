import PySimpleGUI as sg
import functions as f

sites = ['facebook.com','orkut.com','microsoft.com','ubuntu.com','apple.com','google.com','wikipedia.com']
status,imagem = '',''

def janela_inicial():
    sg.theme('Reddit')
    layout = [
                [sg.Combo(sites,key='site',s=(80,8)),
                 sg.Button('Enviar')],
                [sg.Radio('OK', 1,enable_events=True, key='on',default=True),
                 sg.Radio('Sem Conexão', 1,enable_events=True, key='off'),
                 sg.Radio('Servidor Offline', 1,enable_events=True, key='server_off'),
                 sg.Radio('Autenticação Falhou', 1,enable_events=True, key='auth')],
                [sg.Image(r'%s' % (imagem))]
            ]
    return sg.Window('Simulador HTTP', layout, finalize=True)

def janela_request(site):
    sg.theme('Reddit') 
    layout = [
                [sg.Multiline(f.enviar_request(site), s=(70,20))],
                [sg.Button('OK')]
            ]
    return sg.Window('REQUEST', layout, finalize=True)
    
janela1,janela2,janela3 = janela_inicial(), None, None

def janela_response(site):
    sg.theme('Reddit')
    layout = [
                [sg.Multiline(f.receber_response(site), s=(70, 20))],
                [sg.Button('OK')]
            ]
    return sg.Window('RESPONSE', layout, finalize=True)


while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    if window == janela1 and event == 'Enviar':
        site = values['site']
        status = f.verificar_botao()
        janela2 = janela_request(site)
    if window == janela2 and event == 'OK':
        janela2.hide()
        janela3 = janela_response(site)
        imagem = f.carregar_response(imagem,site)
    if window == janela3 and event == 'OK':
        janela1.hide()
        janela1 = janela_inicial()   
        janela2.hide()
        janela3.hide()
        