/*! React Starter Kit | MIT License | http://www.reactstarterkit.com/ */

import React, { PropTypes } from 'react';
import styles from './ContentPage.css';
import withStyles from '../../decorators/withStyles';

@withStyles(styles)
class ContentPage {

  static propTypes = {
    path: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,
    title: PropTypes.string
  };

  static contextTypes = {
    onSetTitle: PropTypes.func.isRequired
  };

  render() {
    this.context.onSetTitle(this.props.title);
    return (
      <div className="ContentPage">
        <div className="BipCardIdForm">
          <b><label for='bip_card_id'>Nº bip!:&nbsp;&nbsp;</label></b><input id='bip_card_id' name='bip_card_id'/>&nbsp;&nbsp;<button name='get_bip_balance'>Obtener</button>
        </div>
      </div>
    );
  }

}

export default ContentPage;
