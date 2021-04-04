import React from 'react';
import './HomePage.css';

class HomePage extends React.Component{
    render() {
        return (
            <div class="home-page">
                <section id="intro">
                    <h2>New Testament App</h2>
                    <blockquote class='main-blockquote'>
                        Welcome! This is a New Testament Web App I created for my New Testament project.
                        This simple application communicates with a public Bible API to retrieve different
                        Bible scriptures. It currently has two different pages: "Scripture Search" and "Search
                        by Topic". "Scripture Search" takes in an input scripture location like "John 3:16" and retrieves
                        the text of the scripture. "Search by Topic" contains a list of different topics we covered
                        this semester and returns a Bible scripture associated with that topic, there are about
                        4-5 scriptures per topic.
                    </blockquote>
                </section>
            </div>
        );
    }
}

export default HomePage;