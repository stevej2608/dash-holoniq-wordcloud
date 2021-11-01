import React, {Component} from 'react';
import randomColor from 'randomcolor';
import PropTypes from 'prop-types';

import TagCloud from 'react-tag-cloud';

/**
 * ExampleComponent is an example component.
 */

export default class DashTagcloud extends Component {
  render() {
    const {label, id, loading_state, setProps, color, hue, children, ...tagcloud_props} = this.props
    const tag_children = React.Children.map(children, (child => <div>{React.cloneElement(child)}</div>))

    if (tagcloud_props.style && tagcloud_props.style.color) {
      const color = tagcloud_props.style.color
      tagcloud_props.style.color = () => randomColor(color)
    }

    return (
      <TagCloud {...tagcloud_props} rotate={60}>
        {tag_children}
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
