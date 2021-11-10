import React, { PureComponent, createRef } from 'react';
import PropTypes from 'prop-types';
import WordCloudJS from 'wordcloud';

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

  constructor(props){
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

  renderWordCloud () {
    const { width, height, ...options} = this.props;
    if (WordCloudJS.isSupported) {
      WordCloudJS(this.canvas.current, {...options});
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

    /**
     * List of words/text to paint on the canvas in a 2-d array, in the form of [word, size].
     *
     * eg. [['foo', 12], ['bar', 6]]
     */

    list: PropTypes.array.isRequired,

    /**
     *
     */

    color: PropTypes.oneOfType([
      PropTypes.string, // CSS color
      PropTypes.object, // null to dissable color inlininig
      PropTypes.func,   // callback(word, weight, fontSize, distance, theta)
    ]),

    /**
     *
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
     *
     */

    ellipticity: PropTypes.number,

    /**
     *
     */

    minSize: PropTypes.number,

    /**
     * calculates initial font size
     */

    weightFactor: PropTypes.number,

    // Dimension

    /**
     * calculates initial font size
     */

    gridSize: PropTypes.number,
    origin: PropTypes.arrayOf(PropTypes.number),
    drawOutOfBound: PropTypes.bool,

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
