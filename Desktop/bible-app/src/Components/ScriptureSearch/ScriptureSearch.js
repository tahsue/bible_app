import React from 'react';
import './ScriptureSearch.css'
import TopicButton from './TopicButton/TopicButton';
import Topics from './scripture-topics.json'

class ScriptureSearch extends React.Component{
    constructor(props) {
        super(props);
        this.state = {
            scripture: ''
        }
    }
    update(value) {
        return () => {
           this.setState({
             scripture: value
           });
        }
    }

    callbackFunction = (childData) => {
        console.log(childData)
        this.setState({scripture: childData})
    }
    
    render() {
        var topics = ['Faith', 'Hope', 'Chairity', 'Service', 'Honesty', 'Sacrament', 'Atonement', 'Family', 
                        'Fasting', 'Missionary Work', 'Obedience', 'Tithing', 'Scriptures', 'Baptism', 'Jesus Christ']
        topics.sort()
        return (
            <div class="search-page">
                <div class="buttons">
                    {
                        topics.map((topic, i) =>  {
                            return <TopicButton parentCallback = {this.callbackFunction} data={this.update.bind(this)} name={topic} />
                        })
                    }
                </div>
                <blockquote class='otro-blockquote'>
                    {this.state.scripture.text}
                    <span>{this.state.scripture.reference}</span>
                </blockquote>
            </div>
        );
    }
}

export default ScriptureSearch;