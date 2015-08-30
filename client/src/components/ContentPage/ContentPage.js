/*! React Starter Kit | MIT License | http://www.reactstarterkit.com/ */

import React, { PropTypes, Component } from 'react';
import styles from './ContentPage.css';
import withStyles from '../../decorators/withStyles';

@withStyles(styles)
class ContentPage extends Component {

  static propTypes = {
    path: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
    title: PropTypes.string
  };

  static contextTypes = {
    onSetTitle: PropTypes.func.isRequired
  };

  constructor() {
    super();
    this.state = {balance: { date: '', amount: '' }, load_state: 'Ingrese un número de tarjeta valido'};
  }

  render() {
    this.context.onSetTitle(this.props.title);
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
  }

  getBalance() {
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
}

export default ContentPage;
