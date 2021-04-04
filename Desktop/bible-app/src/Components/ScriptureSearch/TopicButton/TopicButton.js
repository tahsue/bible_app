import React from 'react';
import './TopicButton.css';
import Topics from '../scripture-topics.json';

class TopicButton extends React.Component{
    
    getRandNum(name) {
        console.log(Topics[name])
        var number = Math.floor(Math.random() * Topics[name].length);
        return number;
    }

    encodeScripture(scripture) {
        return scripture.replace(" ", "%20");
    }

    getScriptureInfo(topic) {
        this.props.data(this.state.scripture)
        var number = this.getRandNum(topic);
        var scripture = this.encodeScripture(Topics[topic][number]);
        var scriptureEndpoint = "https://bible-api.com/" + scripture
        fetch(scriptureEndpoint).then(response => response.json())
        // .then(data => console.log(data.text))
        .then(data => this.props.parentCallback(data));
    }

    constructor(props) {
        super(props);
        this.state = {
            // scripture: "test"
        }
    }

    render() {
        return (
            <div class="button">

              <button onClick={() => this.getScriptureInfo(this.props.name)}>{this.props.name}</button>

            </div>
        );
    }

    
}

export default TopicButton;