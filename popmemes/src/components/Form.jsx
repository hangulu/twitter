import React, { Component } from 'react';
import ImageService from '../ImageService';

// Instantiate the ImageService module
const imservice = new ImageService();

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {value: '', user: '', image: '', freq: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleKeyUp = this.handleKeyUp.bind(this);
  }

  // Handle the submission of the form
  handleSubmit(event) {
    event.preventDefault();
    const user = this.state.value
    var self = this;
    // Post the username
    imservice.createPopimage(user)
      .then(res => self.setState({user: res.data['user'], image: res.data['pop_img'], freq: res.data['freq']}));
  }

  // Change the value of the state on every keypress
  handleChange(event) {
    this.setState({value: event.target.value});
  }

  // Allow one to submit the form by hitting Enter
  handleKeyUp(event) {
    if (event.keyCode === 13) return this.sendData();
  }

  // Clear the form and allow a new user to be entered
  newUser(event) {
    this.setState({value: '', user: '', image: '', freq: ''});
  }

  render() {
    var self = this;
    // If the form has not been filled, allow it to be filled
    if (self.state.user === '') {
      return (
        <form onSubmit={this.handleSubmit} onKeyUp={this.handleKeyUp}>
          <label>
            <input type="text" value={this.state.value} onChange={this.handleChange} class="form-control" />
          </label>
          <input type="submit" value="Submit" class="form-control btn-success" />
        </form>
      );
    } else {
      // Allow the user to reload the form
      return (
        <div>
          <p>
            The most popular image on the timeline of Twitter user @{self.state.user} is {self.state.image} with a frequency of {self.state.freq}%.
          </p>

          <form onSubmit={this.newUser}>
            <input type="submit" value="New User" class="form-control btn-success" />
          </form>
        </div>
      );
    }
  }
}

export default Form;
