import React, {Component} from 'react';
import randomColor from 'randomcolor';
import PropTypes from 'prop-types';

import TagCloud from 'react-tag-cloud';

/**
 * This is a Dash wrapper for the Wordle-inspired word cloud layout. It uses HTML5
 * canvas and sprite masks to achieve near-interactive speeds.
 *
 * See https://github.com/IjzerenHein/react-tag-cloud
 *
 * See also https://github.com/jasondavies/d3-cloud
 */

export default class DashTagcloud extends Component {

  constructor(props){
    super(props);
    this.onclick = false
    this.handleClick = this.handleClick.bind(this)
    this.add_wrapper = this.add_wrapper.bind(this)
  }

  handleClick(e) {
    // console.log('DashTagcloud.handleClick')
    e.stopPropagation();
    e.nativeEvent.stopImmediatePropagation();
    this.onclick = true
  }

  shouldComponentUpdate(nextProps, nextState) {

    // Click events on any child cause the entire cloud to
    // update. This results in new layout with new colors. This
    // behaviour is not intended and only happens when the react
    // TagCloud component is managed by Dash. To stop this
    // the click event sets a flag that we test here. If it's
    // set we dismiss the update

    const update = !this.onclick
    this.onclick = false
    // console.log('DashTagcloud.shouldComponentUpdate=%s', update)
    return update
  }

  add_wrapper(child) {

    const props = child.props._dashprivate_layout.props || child.props

    let text = props.text;

    if (!text) {
        const children = props.children;
        text = Array.isArray(children) ? children[0] : children;
    }

    text = '' + text

    const wrapper = <div {...props} >{text}</div>
    return wrapper

  }

  render() {

    // console.log('DashTagcloud.render')

    const {label, id, loading_state, setProps, color, hue, random=0, children, ...tagcloud_props} = this.props
    // const tag_children = React.Children.map(children, (child) => this.add_wrapper(child))

    if (tagcloud_props.style && tagcloud_props.style.color) {
      const color = tagcloud_props.style.color
      tagcloud_props.style.color = () => randomColor(color)
    }

    const _random = random

    tagcloud_props.random = () => {
      return _random? Math.random(_random) : 0
      }

    return (
      <TagCloud {...tagcloud_props} onClick={this.handleClick}>
        {children}
      </TagCloud>
    )
  }
}

DashTagcloud.defaultProps = {};

DashTagcloud.propTypes = {
  /**
    * The ID used to identify this component in Dash callbacks.
    */
  id: PropTypes.string,

  /**
   * The children of this component
   */
  children: PropTypes.node,

  /**
   * Defines CSS styles which will override styles previously set.
   */
  style: PropTypes.object,

  /**
   * Rotation in degrees
   */

  rotate: PropTypes.number,

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
