import React, {Component} from 'react';
import randomColor from 'randomcolor';
import PropTypes from 'prop-types';

import WordCloud from 'react-d3-cloud';

/**
 * This is a Dash wrapper for treact-d3-cloud.
 *
 * See https://github.com/Yoctol/react-d3-cloud
 *
 */

export default class DashTagcloud extends Component {

  constructor(props){
    super(props);
  }

  handleClick = (e) => {
    e.stopPropagation();
    e.nativeEvent.stopImmediatePropagation();
    console.log(`onWordClick: ${d.text}`);
  }

  render() {
    const {label, id, loading_state, setProps, fontSize, ...cloud_props} = this.props

    cloud_props.fontSize = (word) => Math.log2(word.value) * fontSize

    return (
      <WordCloud {...cloud_props} onWordClick={this.onWordClick} />
    )
  }
}

DashTagcloud.defaultProps = {
  rotate : 0,
  fontSize : 10
};

DashTagcloud.propTypes = {
  /**
    * The ID used to identify this component in Dash callbacks.
    */
  id: PropTypes.string,

  /**
   * Array of words to be displayed with word frequency
   */

  data: PropTypes.arrayOf(PropTypes.shape({
      text: PropTypes.string.isRequired,
      value: PropTypes.number.isRequired,
    })).isRequired,


  /**
   * Rotation in degrees
   */

  rotate: PropTypes.number,


  /**
   *
   */

  fontSize: PropTypes.number,

  /**
   *
   */

  random: PropTypes.number,

  /**
   * Spiral 'archimedean'| 'rectangular'
   */

  spiral: PropTypes.string,


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
