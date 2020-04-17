import React from "react";
import ReactDom from "react-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars } from "@fortawesome/free-solid-svg-icons";
import PropTypes from "prop-types";
import NavLinks from "./Navlinks";
const Navbar = () => {
  return (
    <React.Fragment>
      <div className="navbar" id="navigation">
        <a className="navbar-brand">Gulani</a>
        <span id="top-bars">
          <FontAwesomeIcon icon={faBars} size="2x" />
        </span>
        <div className="d-flex flex-column" id="search-form-holder">
          <form id="search-form">
            <input
              className="form-control"
              type="text"
              placeholder="search for items..."
            />
            <button className="btn">search</button>
          </form>
        </div>
      </div>
      <div className="middle-div">
        <div className="navbar-list">
          <div id="top-list">
            <ul className="mb-0">
              <NavLinks />
              {/* <li>
                <a href="#">Home</a>
              </li>
              <li>
                <a href="#">About</a>
              </li>
              <li>
                <a href="#">Help</a>
              </li>
              <li>
                <a href="#">Contact</a>
              </li>
              <li>
                <a href="#">Home</a>
              </li>
              <li>
                <a href="#">Home</a>
              </li> */}
            </ul>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
};

ReactDom.render(<Navbar />, document.getElementById("navbar"));
