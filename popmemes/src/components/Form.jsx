import React, { Component } from 'react';
import axios from "axios";

class Form extends Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleKeyUp = this.handleKeyUp.bind(this);
  }

  // Buffer between submission and analysis
  analyzing() {
    return (
      <span>
      Analyzing this user's timeline.
      </span>
    );
  }

  // Change the value of the state on every keypress
  handleChange(event) {
    this.setState({value: event.target.value});
  }

  // Handle the submission of the form
  handleSubmit(event) {
    alert('Now analyzing the following Twitter user: @' + this.state.value);
    event.preventDefault();
    axios
      .post("http://localhost:8000/api/popmemes/", event)
      .then(res => this.analyzing());
  }

  // Allow one to submit the form by hitting Enter
  handleKeyUp(event) {
    if (event.keyCode == 13) return this.sendData();
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
