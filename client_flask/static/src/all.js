//Creating Space Names
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
    o.app = function(){
        bipbalance_client.UI.init();
    }
})(bipbalance_client.common);

(function (o) {
    o.widgets = o.widgets || {};
    var _instances = {};

    o.addInstance = function(key, instance){
        _instances[key] = instance;
    }

    o.getInstance = function(key){
        return _instances[key];
    }

    o.init = function () {
        React.render(
          <bipbalance_client.UI.widgets.GetBalance />,
          document.getElementById('get_balance')
        );
    };
})(bipbalance_client.UI);

(function (o) {
    o.GetBalance = React.createClass({
      load: function(url) {

      },
      componentWillMount: function() {
        this.load();
      },
      getInitialState: function() {
        return this.state = {balance: { date: '', amount: '' }, load_state: 'Ingrese un número de tarjeta valido'};
      },
      componentDidMount: function() {

      },
      render: function() {
        return (
         <div className="ContentPage">
            <div className="BipCardIdForm">
              <div>
              <b><label for='bip_card_id'>Nº bip!:&nbsp;&nbsp;</label></b>
              <input id='bip_card_id' name='bip_card_id' ref="bip_card_id"/>&nbsp;&nbsp;
              <button name='get_bip_balance' onClick={this.getBalance.bind(this)}>Obtener</button>
              </div>
              <div>
                  {this.state.load_state}
              </div>
            </div>
            <div className="BipCardBalanceForm">
                <div><b>Saldo Tarjeta:</b> {this.state.balance.amount}</div>
                <div><b>Fecha Saldo:</b> {this.state.balance.date}</div>
            </div>
          </div>
        );
      },
      getBalance: function() {
        this.setState({load_state: 'Obteniendo ...'});
        var bip_card_id = React.findDOMNode(this.refs.bip_card_id).value.trim();
        $.ajax({
          url: 'http://127.0.0.1:8000/bip/balance/' + bip_card_id,
          dataType: 'json',
          crossDomain: true,
          cache: false,
          success: function(data) {
            this.setState({balance: data});
            this.setState({load_state: 'Saldo Actualizado!'});
          }.bind(this),
          error: function(xhr, status, err) {
            this.setState({load_state: 'No se pudo obtener el saldo. Verifique que el número de tarjeta ingresado es correcto'});
            console.error(this.props.url, status, err.toString());
          }.bind(this)
        });
      }
    });
})(bipbalance_client.UI.widgets);

$(document).ready(function () {
    bipbalance_client.common.app();
});
