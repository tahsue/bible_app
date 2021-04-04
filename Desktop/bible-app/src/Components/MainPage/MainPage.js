import React from 'react';
import Navbar from '../Navbar/Navbar'
import ScriptureSearch from '../ScriptureSearch/ScriptureSearch'
import HomePage from '../HomePage/HomePage'
import SearchPage from '../SearchPage/SearchPage'
import './MainPage.css';

class MainPage extends React.Component{
    
    constructor(props) {
        super(props);
        this.state = {
            page: 'main'
        }
    }

    update(value) {
        return () => {
           this.setState({
             page: value
           });
        }
    }

    callbackFunction = (childData) => {
        console.log(childData)
        this.setState({page: childData})
    }

    render() {
        let widget;
        if (this.state.page == "scripture-search-topic") {
            widget = <ScriptureSearch />
        }
        else if (this.state.page == "scripture-search") {
            widget = <SearchPage />
        }
        else {
            widget = <HomePage />
        }
        return (
            <div className="App" class="app">
                <Navbar parentCallback = {this.callbackFunction} />
                {widget}
            </div>
        );
    }
}

export default MainPage;