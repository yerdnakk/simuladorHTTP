import site
import textwrap
import requests
import simulador as sim

def request(response, *args, **kwargs):
    global requisicao
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    requisicao = (textwrap.dedent('''{req.method} {req.url} HTTP/1.1
{reqhdrs}
    ''').format(
        req=response.request, 
        reqhdrs=format_headers(response.request.headers) 
    ))
        
def enviar_request(site):
    global teste
    teste = requests.get('http://' + site, headers={"User-Agent": "EXERCICIO UNIDAVI"}, hooks={'response': request})
    return requisicao 

def response(response, *args, **kwargs):
    global resposta
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    resposta = (textwrap.dedent('''''' + status_code(sim.status) + '''
{reshdrs}''').format(
        res=response, 
        reshdrs=format_headers(response.headers)
    ))

def status_code(opt):
    switch = {
        0: "200 OK",
        1: "408 REQUEST TIMED OUT",
        2: "502 BAD GATEWAY",
        3: "401 UNAUTHORIZED",
        4: "500 INTERNAL SERVER ERROR"
    }
    
    return switch.get(opt)

def receber_response(site):
    global resp
    if sim.status == 0:
        resp = requests.get('http://' + site, headers={"User-Agent": "EXERCICIO UNIDAVI"}, hooks={'response': response})
    else:
        resp = requests.get('http://' + site, headers={"User-Agent": "EXERCICIO UNIDAVI", "connection": "close"}, hooks={'response': response})
    return resposta

def carregar_response(img,site):
    if sim.status == 0:   
        img = r'img\%s.png' % (site)
    else:
        img = ''
    return img

def verificar_botao():
    if sim.site == 'orkut.com':
        return 4
    elif sim.values['off']:
        return 1
    elif sim.values['server_off']:
        return 2
    elif sim.values['auth']: 
        return 3
    elif sim.values['on'] :
        return 0  
    

    
