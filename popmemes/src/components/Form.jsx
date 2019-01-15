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
    axios
      // Get the meme with the specified username
      .get("http://localhost:8000/api/popmemes/", {params: {user: this.state.value}})
      // Handle the response
      .then(response => this.setState({ memeList: res.data }))
      .catch(error => console.log(err));
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
      .then(response => this.analyzing());
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
