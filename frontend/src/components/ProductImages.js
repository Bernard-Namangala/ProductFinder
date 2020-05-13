import * as React from "react";

import ImageUploading from "react-images-uploading";
// { ImageUploadingPropsType, ImageListType, ImageType } is type for typescript

const maxNumber = 10;
const maxMbFileSize = 5;
const ProductImages = ({ onChangeOfImagelist }) => {
  return (
    <ImageUploading
      onChange={onChangeOfImagelist}
      maxNumber={maxNumber}
      multiple
      maxFileSize={maxMbFileSize}
      acceptType={["jpg", "gif", "png"]}
    >
      {({ imageList, onImageUpload, onImageRemoveAll, errors }) => (
        // write your building UI
        <div>
          <button onClick={onImageUpload}>Upload images</button>
          <button onClick={onImageRemoveAll}>Remove all images</button>
          <div className="product-images-holder">
            {imageList.map((image) => (
              <div className="image-holder" key={image.key}>
                <div className="dark-bg">
                  <button
                    type="button"
                    className="remove-image"
                    aria-hidden="true"
                    onClick={image.onRemove}
                  >
                    &times;
                  </button>
                </div>
                <img src={image.dataURL} className="product-image" />

                {/* <button onClick={image.onUpdate}>Update</button>
              <button onClick={image.onRemove}>Remove</button> */}
              </div>
            ))}
          </div>
          <div>
            {errors.maxNumber && (
              <span>Number of selected images exceed maxNumber</span>
            )}
            {errors.acceptType && (
              <span>Your selected file type is not allowed</span>
            )}
            {errors.maxFileSize && (
              <span>Selected file size exceeds maxFileSize</span>
            )}
          </div>
        </div>
      )}
    </ImageUploading>
  );
};

export default ProductImages;
