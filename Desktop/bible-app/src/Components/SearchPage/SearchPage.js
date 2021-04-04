import React from 'react';
import './SearchPage.css';

class SearchPage extends React.Component{
    constructor(props) {
        super(props);
        this.state = {value: '', scripture: '', reference: ''};
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {    
        this.setState({value: event.target.value});  
    }
    handleSubmit(event) {
        // this.setState({scripture: "changed scripture"})
        this.getScriptureInfo(this.state.value)
        event.preventDefault();
    }

    encodeScripture(scripture) {
        return scripture.replace(" ", "%20");
    }
    getScriptureInfo(location) {
        var scripture = this.encodeScripture(location);
        var scriptureEndpoint = "https://bible-api.com/" + scripture
        fetch(scriptureEndpoint).then(response => response.json())
        .then(data => this.checkScripture(data));
    }
    checkScripture(data) {
        if (data.error) {
            this.setState({scripture: "Please enter a valid scripture"})
            return;
        }
       
        else {
            this.setState({scripture: data.text})
            this.setState({reference: data.reference})
        }
    }
    render() {
        return (
            <div class="search-page">
                <form onSubmit={this.handleSubmit}>
                    <label>
                    Seach a Scripture:&nbsp;&nbsp;
                    <input type="text" value={this.state.value} onChange={this.handleChange} />        </label>
                    &nbsp;&nbsp;
                    <input type="submit" value="Search" />
                </form>
                <blockquote class='search-blockquote'>
                    {this.state.scripture}
                    <span>{this.state.reference}</span>
                </blockquote>
            </div>
        );
    }
}

export default SearchPage;