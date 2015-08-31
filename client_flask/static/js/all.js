//Creating Space Names
'use strict';

var bipbalance_client = bipbalance_client || {};

(function (o) {
  o.utils = o.utils || {};
  o.params = o.params || {};
  o.UI = o.UI || {};
  o.common = o.common || {};
  o.i18n = o.i18n || {};
  o.security = o.security || {};
  o.shares = o.shares || {};
})(bipbalance_client);

(function (o) {
  o.app = function () {
    bipbalance_client.UI.init();
  };
})(bipbalance_client.common);

(function (o) {
  o.widgets = o.widgets || {};
  var _instances = {};

  o.addInstance = function (key, instance) {
    _instances[key] = instance;
  };

  o.getInstance = function (key) {
    return _instances[key];
  };

  o.init = function () {
    React.render(React.createElement(bipbalance_client.UI.widgets.GetBalance, null), document.getElementById('get_balance'));
  };
})(bipbalance_client.UI);

(function (o) {
  o.GetBalance = React.createClass({
    displayName: 'GetBalance',

    load: function load(url) {},
    componentWillMount: function componentWillMount() {
      this.load();
    },
    getInitialState: function getInitialState() {
      return this.state = { balance: { date: '', amount: '' }, load_state: 'Ingrese un número de tarjeta valido' };
    },
    componentDidMount: function componentDidMount() {},
    render: function render() {
      return React.createElement(
        'div',
        { className: 'ContentPage' },
        React.createElement(
          'div',
          { className: 'BipCardIdForm' },
          React.createElement(
            'div',
            null,
            React.createElement(
              'b',
              null,
              React.createElement(
                'label',
                { 'for': 'bip_card_id' },
                'Nº bip!:  '
              )
            ),
            React.createElement('input', { id: 'bip_card_id', name: 'bip_card_id', ref: 'bip_card_id' }),
            '  ',
            React.createElement(
              'button',
              { name: 'get_bip_balance', onClick: this.getBalance.bind(this) },
              'Obtener'
            )
          ),
          React.createElement(
            'div',
            null,
            this.state.load_state
          )
        ),
        React.createElement(
          'div',
          { className: 'BipCardBalanceForm' },
          React.createElement(
            'div',
            null,
            React.createElement(
              'b',
              null,
              'Saldo Tarjeta:'
            ),
            ' ',
            this.state.balance.amount
          ),
          React.createElement(
            'div',
            null,
            React.createElement(
              'b',
              null,
              'Fecha Saldo:'
            ),
            ' ',
            this.state.balance.date
          )
        )
      );
    },
    getBalance: function getBalance() {
      this.setState({ load_state: 'Obteniendo ...' });
      var bip_card_id = React.findDOMNode(this.refs.bip_card_id).value.trim();
      $.ajax({
        url: 'http://127.0.0.1:8000/bip/balance/' + bip_card_id,
        dataType: 'json',
        crossDomain: true,
        cache: false,
        success: (function (data) {
          this.setState({ balance: data });
          this.setState({ load_state: 'Saldo Actualizado!' });
        }).bind(this),
        error: (function (xhr, status, err) {
          this.setState({ load_state: 'No se pudo obtener el saldo. Verifique que el número de tarjeta ingresado es correcto' });
          console.error(this.props.url, status, err.toString());
        }).bind(this)
      });
    }
  });
})(bipbalance_client.UI.widgets);

$(document).ready(function () {
  bipbalance_client.common.app();
});