import React from 'react';
import './App.css';

import { BrowserRouter as Router } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';

import Home from "./Home.js";

// React Header function
function Header() {

    const useStyles = makeStyles((theme) => ({
        title: {
            marginRight: theme.spacing(2),
            color: "#ffc500!important",
            textAlign: 'left',
            flex: 1
        },
        navButton: {
            textAlign: 'right',
            alignSelf: 'stretch'
        },
        navIcon: {
            padding: '5px',
            width: '35px'
        }
    }));

    const classes = useStyles();

    // returning react header ui view component
    return (
        <Router>
            {/* <AppBar position="static">
                <Toolbar className="toolbar">
                    <Typography variant="h6" className={classes.title}>
                        UI
          </Typography>
                    <Button component={Link} to='/' color="inherit" className={classes.navButton}>Home</Button>
                </Toolbar>
            </AppBar> */}
            {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
            
        </Router>
    );

}

export default Header;
