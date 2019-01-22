import React, { Component } from 'react';
import ImageService from '../ImageService';

// Instantiate the ImageService module
const imservice = new ImageService();

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {value: '', user: '', image: '', freq: ''};

    this.displayData = this.displayData.bind(this);
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleKeyUp = this.handleKeyUp.bind(this);
  }

  // Handle the submission of the form
  handleSubmit() {
    const user = this.state.value
    var self = this;
    // Post the username
    imservice.createPopimage(user)
      .then(res => self.setState({user: res.data['user'], image: res.data['pop_img'], freq: res.data['freq']}))
      .then(() => self.displayData());
  }

  // Display a user's data
  displayData() {
    var self = this;
    alert('The most popular image on the timeline of Twitter user @' + self.state.user + ' is ' + self.state.image + ', with a frequency of ' + self.state.freq + '%.');
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
