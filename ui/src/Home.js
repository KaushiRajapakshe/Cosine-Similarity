// src/components/bootstrap-carousel.component.js
import React from "react";

import Avatar from "@material-ui/core/Avatar";
import 'bootstrap/dist/css/bootstrap.min.css';
import styled from "styled-components";

const WhiteAvatar = styled(Avatar)`
  background-color: white;
  width: 150px;
  height: 150px;
  
`;

class Home extends React.Component {

    render() {
        return (
            <div className="home">
                <div className='container-fluid' >
                    <div className="row">
                        <div className="col-12">
                            
                        </div>
                    </div>
                </div>
                <div className="home-content">
                <WhiteAvatar>G</WhiteAvatar>
                    <h2 className="home-title"><b>Join with Vidu Mithura App</b></h2>
                    <p className="home-description">Hi</p>
                </div>
            </div>
        )
    };
}

export default Home;