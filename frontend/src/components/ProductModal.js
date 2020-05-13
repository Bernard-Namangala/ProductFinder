import React, { Component } from "react";

import ProductImages from "./ProductImages";
class ProductModal extends Component {
  state = {
    feature_name: "",
    feature_value: "",
    product: {
      name: "",
      description: "",
      features: [],
      price: 0,
      negotiable: 0,
      images: [],
    },
  };
  constructor(props) {
    super(props);
  }

  productNameChange = (e) => {
    this.setState({
      product: {
        ...this.state.product,
        name: e.target.value,
      },
    });
  };

  productDescriptionChange = (e) => {
    this.setState({
      product: {
        ...this.state.product,
        description: e.target.value,
      },
    });
  };

  productPriceChange = (e) => {
    this.setState({
      product: {
        ...this.state.product,
        price: e.target.value,
      },
    });
  };

  productNegotiabilityChange = (e) => {
    let negotiable = 0;
    if (e.target.checked) {
      negotiable = 1;
    }
    this.setState({
      product: {
        ...this.state.product,
        negotiable: negotiable,
      },
    });
  };

  featureNameChange = (e) => {
    this.setState({
      feature_name: e.target.value,
    });
  };

  featureValueChange = (e) => {
    this.setState({
      feature_value: e.target.value,
    });
  };

  addFeature = (e) => {
    e.preventDefault();
    let feature_name = this.state.feature_name;
    let feature_value = this.state.feature_value;
    let feature_error_holder = document.getElementById("add-feature-errors");

    if (feature_name.length && feature_value.length) {
      feature_name = `${this.state.feature_name[0].toUpperCase()}${this.state.feature_name.slice(
        1
      )}`;
      let existing_feature = this.state.product.features.filter(
        (key, index) => Object.keys(key)[0] === feature_name
      );
      if (existing_feature.length > 0) {
        feature_error_holder.textContent = `feature "${feature_name}" already exists`;
      } else {
        feature_error_holder.textContent = "";
        this.setState({
          product: {
            ...this.state.product,
            features: [
              ...this.state.product.features,
              { [feature_name]: feature_value },
            ],
          },
        });
      }
    } else {
      if (feature_error_holder) {
        feature_error_holder.textContent =
          "please fill in both feature name and feature value";
      }
    }
  };

  removeFeature = (id) => {
    let array_of_product_features = this.state.product.features;
    let filtered_array = array_of_product_features.filter(
      (item, index) => index !== id
    );
    this.setState({
      product: {
        ...this.state.product,
        features: filtered_array,
      },
    });
  };

  submitHandler = (e) => {
    e.preventDefault();
  };

  onChangeOfImagelist = (imagelist) => {
    this.setState({
      product: {
        ...this.state.product,
        images: imagelist,
      },
    });
  };
  render() {
    return (
      <div
        className="modal fade"
        id="upload-product-modal"
        tabIndex="-1"
        role="dialog"
        aria-labelledby="myModalLabel"
        aria-hidden="true"
      >
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h4 className="modal-title" id="myModalLabel">
                Add a new product to your store
              </h4>
              <button
                type="button"
                className="close"
                data-dismiss="modal"
                aria-hidden="true"
              >
                &times;
              </button>
            </div>
            <div className="modal-body">
              <form onSubmit={this.submitHandler}>
                <div className="form-group">
                  <input
                    type="text"
                    className="form-control"
                    placeholder="Product Name"
                    onChange={this.productNameChange}
                  />
                </div>
                <div className="form-group">
                  <ProductImages
                    onChangeOfImagelist={this.onChangeOfImagelist}
                  />
                </div>
                <div className="form-group">
                  <textarea
                    className="form-control"
                    placeholder="product description"
                    onChange={this.productDescriptionChange}
                  ></textarea>
                </div>

                <div className="add-product-feature form-group">
                  <div className="add-feature-input-boxes">
                    <input
                      type="text"
                      className="form-control"
                      placeholder="feature name"
                      onChange={this.featureNameChange}
                    />

                    <input
                      type="text"
                      className="form-control"
                      placeholder="feature value"
                      onChange={this.featureValueChange}
                    />
                    <button
                      className="btn secondary-background"
                      id="add-feature-button"
                      onClick={this.addFeature}
                    >
                      Add feature
                    </button>
                  </div>
                  <div className="feature-example">
                    <span className="text-center text-success">
                      *eg...Ram : 4GB
                    </span>
                  </div>
                  <div
                    className="add-feature-errors text-danger"
                    id="add-feature-errors"
                  ></div>
                </div>
                <ul id="product-features" className="form-group">
                  {this.state.product.features.map((key, index) =>
                    Object.keys(key).map((item) => (
                      <li key={item}>
                        <span className="feature-name-holder">{item}</span>:
                        <span className="feature-value-holder">
                          {key[item]}
                        </span>
                        <button
                          type="button"
                          className="remove-feature-button"
                          onClick={() => this.removeFeature(index)}
                        >
                          &times;
                        </button>
                      </li>
                    ))
                  )}
                </ul>
                <div className="input-group mb-3">
                  <div className="input-group-prepend">
                    <span className="input-group-text primary-background">
                      K
                    </span>
                  </div>
                  <input
                    type="number"
                    min="0"
                    id="product-price-input"
                    className="form-control w-60"
                    aria-label="Amount (to the nearest kwacha)"
                    placeholder="Price"
                    onChange={this.productPriceChange}
                  />
                </div>
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value=""
                    id="negotiable-checkbox"
                    onChange={this.productNegotiabilityChange}
                  />
                  <label
                    className="form-check-label"
                    htmlFor="negotiable-checkbox"
                  >
                    Negotiable
                  </label>
                </div>
              </form>
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-default"
                data-dismiss="modal"
              >
                Close
              </button>
              <button type="button" className="btn secondary-background">
                Upload product
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default ProductModal;
