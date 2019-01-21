import React, { Component } from 'react';
import axios from "axios";
import ImageService from '../ImageService';

// Instantiate the ImageService module
const imservice = new ImageService();

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {value: '', user: '', image: '', freq: ''};

    this.componentDidMount = this.componentDidMount.bind(this);
    this.displayData = this.displayData.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleKeyUp = this.handleKeyUp.bind(this);
  }

  // Called when the component is created and inserted into the DOM
  componentDidMount() {
    var self = this;
    imservice.getPopmemes()
      .then(result => self.setState({image: 'No Image'}));
  }

  // Handle the submission of the form
  handleSubmit() {
    const user = this.state.value
    var self = this;
    // alert('Now analyzing the Twitter user @' + user);
    // Post the meme with the username
    imservice.createPopmeme(user)
      .then(() => self.setState({user: user}))
      .then(() => self.displayData(self.state.user));
  }

  // Display a user's data
  displayData(user) {
    var self = this;
    imservice.getPopmeme(user)
      // Set the properties using the response dictionary
      .then(res => console.log(res.data));
      // .then(res => self.setState({image: res['pop_img'], freq: res['freq']}))
      // .then(() => alert("The most popular image on @" +  self.state.user + "'s timeline is " + self.state.image + " with a frequency of " + self.state.freq + "."))
      // .catch(err => console.log(err));
  }

  // Change the value of the state on every keypress
  handleChange(event) {
    this.setState({value: event.target.value});
  }

  // Allow one to submit the form by hitting Enter
  handleKeyUp(event) {
    if (event.keyCode === 13) return this.sendData();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit} onKeyUp={this.handleKeyUp}>
        <label>
          <input type="text" value={this.state.value} onChange={this.handleChange} class="form-control" />
        </label>
        <input type="submit" value="Submit" class="form-control btn-success" />
      </form>
    );
  }
}

export default Form;
