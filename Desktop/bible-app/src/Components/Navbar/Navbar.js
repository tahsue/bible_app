import React from 'react';
import './Navbar.css';

class Navbar extends React.Component{
    render() {
        return (
            <div class="topnav">

              <a onClick={() => this.props.parentCallback('main')} href="#">Home</a>
              <a onClick={() => this.props.parentCallback('scripture-search')} href="#">Scripture Search</a>
              <a onClick={() => this.props.parentCallback('scripture-search-topic')} href="#">Search by Topic</a>
            
            </div>
        );
    }
}

export default Navbar;