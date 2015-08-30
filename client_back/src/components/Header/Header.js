/*! React Starter Kit | MIT License | http://www.reactstarterkit.com/ */

import React from 'react';
import styles from './Header.css';
import withStyles from '../../decorators/withStyles';
import Link from '../Link';
import Navigation from '../Navigation';

@withStyles(styles)
class Header {

  render() {
    return (
      <div className="Header">
        <div className="Header-container">
          <div className="Header-banner">
            <h1 className="Header-bannerTitle">BIP Balance</h1>
            <p className="Header-bannerDesc">Obtén el Saldo de tu tarjeta bip</p>
          </div>
        </div>
      </div>
    );
  }

}

export default Header;
