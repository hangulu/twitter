import React, { Component } from 'react';
import axios from "axios";

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {value: '', image: '', freq: '', run: 'false'};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleKeyUp = this.handleKeyUp.bind(this);
    this.analyzing = this.analyzing.bind(this);
    this.renderMeme = this.renderMeme.bind(this);
  }

  // Buffer between submission and analysis
  analyzing() {
    axios
      // Get the meme with the specified username
      .get("http://localhost:8000/api/popmemes/", {params: {user: this.state.value}})
      // Handle the response, and set run to true
      .then(res => this.setState({ image: res.data[0], freq: res.data[1], run: true }))
      .then(res => alert("The most popular image on @" +  this.state.value + "'s timeline is " + this.state.image + " with a frequency of " + this.state.freq + "."))
      // .then(res => this.renderMeme())
      .catch(err => console.log(err));
  };

  // Change the value of the state on every keypress
  handleChange(event) {
    this.setState({value: event.target.value});
  }

  // Handle the submission of the form
  handleSubmit(event) {
    alert('Now analyzing the following Twitter user: @' + this.state.value);
    event.preventDefault();
    axios
      // Post the meme with the username
      .post("http://localhost:8000/api/popmemes/", {user: this.state.value})
      .then(res => this.analyzing());
  }

  // Allow one to submit the form by hitting Enter
  handleKeyUp(event) {
    if (event.keyCode === 13) return this.sendData();
  }

  renderMeme() {
    // Make variables to store the image and frequency
    const image = this.state.image
    const freq = this.state.freq
    const user = this.state.value

    if (this.state.run === true) {
      return (
        <span>
        An analysis of the profile of {user} shows that {image} is the most popular image, with a frequency of {freq}.
        </span>
      );
    } else {
      return (
        <span>
        Waiting on input.
        </span>
      );
    }
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
