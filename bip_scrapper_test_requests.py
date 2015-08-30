import requests

bip_balance_url = 'http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/SesionPortalServlet'

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {
        'accion': '6'
        , 'NumDistribuidor': '99'
        , 'NomUsuario': 'usuInternet'
        , 'NomHost': 'AFT'
        , 'NomDominio': 'aft.cl'
        , 'Trx': ''
        , 'RutUsuario': '0'
        , 'NumTarjeta': '14219394'
        , 'bloqieable': ''
    }

    response = requests.post(bip_balance_url, payload)

    import ipdb; ipdb.set_trace()
