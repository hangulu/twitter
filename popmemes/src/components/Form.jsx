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
    if (event.keyCode === 13) return this.handleSubmit(event);
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
        <div>
          <p>
            Enter the Twitter handle of the user whose timeline you'd like to analyze:
          </p>

          <form onSubmit={this.handleSubmit} onKeyUp={this.handleKeyUp}>
            <label>
              <input type="text" value={this.state.value} onChange={this.handleChange} class="form-control" />
            </label>
            <input type="submit" value="Submit" class="form-control btn-success resize" />
          </form>
        </div>
      );
    } else {
      // Allow the user to reload the form
      if self.state.image === "No Popular Image" {
        return (
          <div>
            <p class="result">
              The most popular image on the timeline of Twitter user @{self.state.user} is below, appearing with a frequency of {self.state.freq}%.
            </p>
            <img class="resize" src={require('../images/popimg.jpg')} alt="The most popular content on the timeline" />
            <div>
              <form onSubmit={this.newUser}>
                <input type="submit" value="New User" class="form-control btn-success resize" />
              </form>
            </div>
          </div>
        );
      } else {
        return (
          <div>
            <p class="result">
              All the images on the timeline of Twitter user @{self.state.user} are unique.
            </p>
          </div>
        );
      }
    }
  }
}

export default Form;
