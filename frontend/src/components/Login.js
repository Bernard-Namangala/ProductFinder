import React from "react";
import ReactDom from "react-dom";
const Login = () => {
  return (
    <input
      type="text"
      name="username"
      autoFocus
      className="form-control input"
      required
      id="id_username"
    ></input>
  );
};

ReactDom.render(<Login />, document.getElementById("login_username"));
