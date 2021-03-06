import React, { PropTypes } from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';
import { Menu, Icon } from 'antd';

import {Global} from '../../../../config/global.js';
const SubMenu = Menu.SubMenu;

import style from './style.less';


class SlideoutMenu extends React.Component {
  constructor(props) {
    super(props);
    let me = this;
  }

  componentDidMount() {

  }

  componentWillUnmount() {
  }
  handleClick(selection){
    let me = this;

    if(selection.key != 'zj'){
      me.setState({
        current: selection.keyPath
      });
      me.props.onClick(selection);
    }

  }

  render() {
    let me = this;
    var result = <div className={style.menuContainer}>
      <Menu
        theme="dark"
        onClick={me.handleClick.bind(me)}
        style={{ width: '100%' }}
        mode="inline"
        >
        <SubMenu key="list" title={<h3><Icon type="home" />VMAX</h3>}>
          <Menu.Item key="index">
            <Link to="/">
              <h3>
                <Icon type="line-chart" />
                Popular
              </h3>
            </Link>
          </Menu.Item>

          <Menu.Item key="star">
            <Link to="/star">
              <h3>
                <Icon type="clock-circle-o" />
                Star
              </h3>
            </Link>

          </Menu.Item>
        </SubMenu>


      </Menu>
    </div>;

    return result;
  }
}

function mapStateToProps({routing}){
  return {
    currentPath: routing.locationBeforeTransitions.pathname
  }
}
export default connect(mapStateToProps)(SlideoutMenu) ;
