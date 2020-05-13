import Navbar from "./Navbar";
import React, { Component } from "react";
import ReactDom from "react-dom";
import { Route, Switch, BrowserRouter, useLocation } from "react-router-dom";
import ProductModal from "./ProductModal";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route
            path="/store/:slug"
            exact
            render={(config) => <ProductModal />}
          />
          {/* <Route
            path="/subjects/:subject(\w+)"
            render={config => <Subject />}
          /> */}
        </Switch>
      </BrowserRouter>
    );
  }
}

ReactDom.render(<App />, document.getElementById("app"));
