from ghost import Ghost

bip_balance_url = 'http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/'

def get_balance(card_id):
    ghost = Ghost()

    with ghost.start() as browser:
        browser.open(bip_balance_url)

        browser.set_field_value("input[id=txtNumTarjeta]", card_id)
        browser.click("input[id=btnEnviar]", expect_loading=True)

        balance_amount, resources = browser.evaluate('document.evaluate("//*[contains(text(), \'Saldo  tarjeta:\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.nextSibling.nextSibling.innerHTML;')
        balance_date, resources = browser.evaluate('document.evaluate("//*[contains(text(), \'Fecha saldo: \')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.nextSibling.nextSibling.innerHTML;')

        return {'amount': balance_amount, 'date': balance_date}

if __name__ == '__main__':
    print get_balance('14219394')

