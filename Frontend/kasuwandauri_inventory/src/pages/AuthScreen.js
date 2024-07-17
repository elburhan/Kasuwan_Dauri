import React, { useState, useEffect } from 'react';
import {
  Box,
  Card,
  CardContent,
  Tabs,
  Tab,
  TextField,
  Button,
  Typography,
} from '@mui/material';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useNavigate } from 'react-router-dom';
import useApi from '../hooks/APIHandler';
import { doSignup } from '../utils/authHelpers'; // Import the doSignup function

const AuthScreen = () => {
  const [tabIndex, setTabIndex] = useState(0);
  const [signupData, setSignupData] = useState({
    username: '',
    email: '',
    password: '',
  });
  const [loginData, setLoginData] = useState({
    username: '',
    password: '',
  });

  const { callApi } = useApi();
  const navigate = useNavigate();

  useEffect(() => {
    if (localStorage.getItem('token')) {
      navigate('/home');
    }
  }, [navigate]);

  const handleTabChange = (event, newIndex) => {
    setTabIndex(newIndex);
  };

  const handleSignupChange = (event) => {
    const { name, value } = event.target;
    setSignupData({
      ...signupData,
      [name]: value,
    });
  };

  const handleLoginChange = (event) => {
    const { name, value } = event.target;
    setLoginData({
      ...loginData,
      [name]: value,
    });
  };

  const doLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await callApi({
        url: 'http://localhost:8000/api/auth/login/',
        method: 'POST',
        body: loginData,
      });
      if (response?.data?.access) {
        localStorage.setItem('token', response.data.access);
        toast.success('Signin Successful');
        navigate('/home');
      } else {
        toast.error('Invalid Credentials');
      }
    } catch (error) {
      toast.error('An error occurred during signin');
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
        backgroundColor: '#f5f5f5',
      }}
    >
      <Card sx={{ minWidth: 275 }}>
        <CardContent>
          <Tabs
            value={tabIndex}
            onChange={handleTabChange}
            variant="fullWidth"
            indicatorColor="primary"
            textColor="primary"
          >
            <Tab label="Login" />
            <Tab label="Signup" />
          </Tabs>
          {tabIndex === 0 && (
            <Box component="form" onSubmit={doLogin} sx={{ mt: 2 }}>
              <Typography variant="h6" gutterBottom>
                Login
              </Typography>
              <TextField
                fullWidth
                label="Username"
                name="username"
                value={loginData.username}
                onChange={handleLoginChange}
                margin="normal"
                variant="outlined"
              />
              <TextField
                fullWidth
                label="Password"
                name="password"
                type="password"
                value={loginData.password}
                onChange={handleLoginChange}
                margin="normal"
                variant="outlined"
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                sx={{ mt: 2 }}
              >
                Login
              </Button>
            </Box>
          )}
          {tabIndex === 1 && (
            <Box component="form" onSubmit={(e) => doSignup(e, signupData, callApi)} sx={{ mt: 2 }}>
              <Typography variant="h6" gutterBottom>
                Signup
              </Typography>
              <TextField
                fullWidth
                label="Username"
                name="username"
                value={signupData.username}
                onChange={handleSignupChange}
                margin="normal"
                variant="outlined"
              />
              <TextField
                fullWidth
                label="Email"
                name="email"
                type="email"
                value={signupData.email}
                onChange={handleSignupChange}
                margin="normal"
                variant="outlined"
              />
              <TextField
                fullWidth
                label="Password"
                name="password"
                type="password"
                value={signupData.password}
                onChange={handleSignupChange}
                margin="normal"
                variant="outlined"
              />
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                sx={{ mt: 2 }}
              >
                Signup
              </Button>
            </Box>
          )}
        </CardContent>
      </Card>
      <ToastContainer
        position="bottom-right"
        autoClose={3000}
        hideProgressBar={false}
        style={{ marginBottom: '30px' }}
      />
    </Box>
  );
};

export default AuthScreen;
