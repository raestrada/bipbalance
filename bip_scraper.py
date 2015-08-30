from ghost import Ghost

bip_balance_url = 'http://pocae.tstgo.cl/PortalCAE-WAR-MODULE/'

if __name__ == '__main__':
    ghost = Ghost()
    browser = ghost.start()

    with ghost.start() as browser:
        page, resources = browser.open(bip_balance_url)

        result, resources = browser.set_field_value("input[id=txtNumTarjeta]", "14219394")
        page, resources = browser.click("input[id=btnEnviar]", expect_loading=True)

        balance_amount, resources = browser.evaluate('document.evaluate("//*[contains(text(), \'Saldo  tarjeta:\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.nextSibling.nextSibling.innerHTML;')
        balance_date, resources = browser.evaluate('document.evaluate("//*[contains(text(), \'Fecha saldo: \')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.nextSibling.nextSibling.innerHTML;')

        balance = { 'amount': balance_amount, 'date': balance_date }

        print balance
