import React, { PureComponent, createRef } from 'react';
import PropTypes from 'prop-types';
import WordCloudJS from 'wordcloud';
import seedRandom from 'seedrandom';

/**
 * This is a Dash wrapper for wordcloud2.js.
 *
 * See https://github.com/timdream/wordcloud2.js
 *
 * Thanks to https://github.com/Tarabyte, this code is a reworked version of
 * https://github.com/Tarabyte/react-wordcloud2/blob/master/src/WordCloud.js
 *
 */

export default class DashTagcloud extends PureComponent {

  constructor(props) {
    super(props);
    console.log('DashTagcloud.constructor')
    this.renderWordCloud = this.renderWordCloud.bind(this)
    this.canvas = createRef();
  }

  componentDidMount() {
    console.log('DashTagcloud.componentDidMount')
    this.renderWordCloud();
  }

  componentDidUpdate() {
    console.log('DashTagcloud.componentDidUpdate')
    this.renderWordCloud();
  }

  renderWordCloud() {
    const { width, height, ...options } = this.props;
    if (WordCloudJS.isSupported) {

      // https://github.com/timdream/wordcloud2.js/issues/138

      if (options.shuffle === false){
        seedRandom('wordcloud2', { global: true });
      }

      WordCloudJS(this.canvas.current, { ...options });
    }
  }

  render() {
    console.log('DashTagcloud.render')
    if (WordCloudJS.isSupported) {
      const { width, height } = this.props;
      return (
        <canvas
          ref={this.canvas}
          style={{ width, height }}
          width={width}
          height={height}
        />
      );
    }

    return <h2>Browser is not supported</h2>
  }

}

DashTagcloud.defaultProps = {
};

// https://github.com/timdream/wordcloud2.js/blob/gh-pages/API.md

DashTagcloud.propTypes = {

  /**
   * Canvas width
   */

  width: PropTypes.number.isRequired,

  /**
   * Canvas height
   */

  height: PropTypes.number.isRequired,

  // Presentation

  /**
   * List of words/text to paint on the canvas in a 2-d array, in the form
   * of [word, size].
   *
   * eg. [['foo', 12], ['bar', 6]]
   *
   * Optionally, you can send additional data as array elements, in the
   * form of '[word, size, data1, data2, ... ]' which can then be
   * used in the callback functions of 'click', 'hover' interactions
   * and fontWeight, color and classes callbacks
   */

  list: PropTypes.array.isRequired,

  /**
   * The font to use
   */

  fontFamily: PropTypes.string,

  /**
   * The font weight to use, can be, as an example, 'normal', 'bold' or '600'
   */

  fontWeight: PropTypes.string,

  /**
   * Color of the text, can be any CSS color
   */

  color: PropTypes.oneOfType([
    PropTypes.string, // CSS color
    PropTypes.object, // null to dissable color inlininig
    PropTypes.func,   // callback(word, weight, fontSize, distance, theta)
  ]),

  /**
   * For DOM clouds, allows the user to define the class of the span elements. Can
   * be a normal class string
   */

  classes: PropTypes.string,

  /**
   * The minimum font size to draw on the canvas.
   */

  minSize: PropTypes.number,

  /**
   * Number to multiply for 'size' of each word in the list.
   */

  weightFactor: PropTypes.number,

  /**
   * Paint the entire canvas with background color and consider
   * it empty before start
   */

  clearCanvas: PropTypes.bool,

  /**
   * The color of the background
   */

  backgroundColor: PropTypes.string,

  // Dimension

  /**
   * The size of the grid in pixels for marking the availability of
   * the canvas — the larger the grid size, the
   * bigger the gap between words
   */

  gridSize: PropTypes.number,

  /**
   * The origin of the “cloud” in [x, y].
   */

  origin: PropTypes.arrayOf(PropTypes.number),

  /**
   * Set to true to allow word being draw partly outside of
   * the canvas. Allow word bigger than the size of the
   * canvas to be drawn.
   */

  drawOutOfBound: PropTypes.bool,

  /**
   * Set to 'true' to shrink the word so it will fit into
   * canvas. Best if 'drawOutOfBound' is set to 'false'. :warning:
   * This word will now have lower 'weight'.
   */

  shrinkToFit: PropTypes.bool,

  // Mask

  /**
   * Visualize the grid by draw squares to mask the drawn areas
   */

  drawMask: PropTypes.number,

  /**
   * Color of the mask squares.
   */

  maskColor: PropTypes.string,

  /**
   * Width of the gaps between mask squares.
   */

  maskGapWidth: PropTypes.number,

  // Rotation

  /**
   * If the word should rotate, the minimum rotation (in rad) the text should rotate
   */

  minRotation: PropTypes.number,

  /**
   * If the word should rotate, the maximum rotation (in rad) the text should rotate. Set the two value equal
   * to keep all text in one angle.
   */

  maxRotation: PropTypes.number,

  /**
   * Force the use of a defined number of angles. Set the value equal to 2 in a -90°/90°
   * range means just -90, 0 or 90 will be used.
   */

  rotationSteps: PropTypes.number,

  // Randomness

  /**
   * Shuffle the points to draw so the result will be different each
   * time for the same list and settings.
   */

  shuffle: PropTypes.bool,

  /**
   * Probability for the word to rotate. Set the number to 1
   * to always rotate.
   */

  rotateRatio: PropTypes.number,

  // Shape

  /**
   * The shape of the "cloud" to draw. Available presents are:
   */

  shape: PropTypes.oneOf([
    'circle',
    'cardioid',
    'diamond',
    'square',
    'triangle',
    'triangle-forward',
    'triangle-upright',
    'pentagon',
    'star',
  ]),

  /**
   * The degree of "flatness" of the shape wordcloud2.js should draw.
   */

  ellipticity: PropTypes.number,

  // Interactive


  // Events


  /**
    * The ID used to identify this component in Dash callbacks.
    */

  id: PropTypes.string,

  /**
   * Often used with CSS to style elements with common properties.
   */

  className: PropTypes.string,

  /**
    * Dash-assigned callback that should be called to report property changes
    * to Dash, to make them available for callbacks.
    */
  setProps: PropTypes.func
};
