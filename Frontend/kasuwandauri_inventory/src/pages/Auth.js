import React, { useState, useMemo, useEffect } from 'react';
import {
  Tabs,
  Tab,
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Box,
  CssBaseline,
  ThemeProvider,
  createTheme,
  LinearProgress,
} from '@mui/material';
import { ThemeProvider as Emotion10ThemeProvider } from '@emotion/react';
import { useTheme } from '@mui/system';
import {
  orangeDarkTheme,
  orangeLightTheme,
  basicTheme,
  darkTheme,
  lightTheme,
  customTheme,
  blueLightTheme,
  blueDarkTheme,
  greenLightTheme,
  greenDarkTheme,
  redLightTheme,
  redDarkTheme,
} from '../layout/themes';
import { GlobalStyles } from '../layout/GlobalStyle';
import { useNavigate } from 'react-router-dom';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import useApi from '../hooks/APIHandler';

const Auth = () => {
  const [tab, setTab] = useState(0);
  const [themeMode, setThemeMode] = useState('basic');
  const [signupData, setSignupData] = useState({
    username: '',
    email: '',
    password: '',
  });
  const [loginData, setLoginData] = useState({
    username: '',
    password: '',
  });

  const { callApi, error, loading } = useApi();
  const navigate = useNavigate();

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'basic';
    setThemeMode(savedTheme);

    if (localStorage.getItem('token')) {
      navigate('/home');
    }
  }, [navigate]);

  const theme = useMemo(() => {
    switch (themeMode) {
      case 'basic':
        return createTheme(basicTheme);
      case 'dark':
        return createTheme(darkTheme);
      case 'light':
        return createTheme(lightTheme);
      case 'custom':
        return createTheme(customTheme);
      case 'blue light':
        return createTheme(blueLightTheme);
      case 'blue dark':
        return createTheme(blueDarkTheme);
      case 'green light':
        return createTheme(greenLightTheme);
      case 'green dark':
        return createTheme(greenDarkTheme);
      case 'red light':
        return createTheme(redLightTheme);
      case 'red dark':
        return createTheme(redDarkTheme);
      case 'orange light':
        return createTheme(orangeLightTheme);
      case 'orange dark':
        return createTheme(orangeDarkTheme);
      default:
        return createTheme(lightTheme);
    }
  }, [themeMode]);

  const handleChange = (event, newValue) => {
    setTab(newValue);
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

  const doSignup = async (e) => {
    e.preventDefault();
    try {
      const response = await callApi({
        url: 'http://localhost:8000/api/auth/signup/',
        method: 'POST',
        body: {
          ...signupData,
          profile_pic: 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png',
        },
      });
      if (response?.data?.access) {
        localStorage.setItem('token', response.data.access);
        toast.success('Signup Successful');
        navigate('/home');
      } else {
        toast.error('Signup failed');
      }
    } catch (error) {
      toast.error('An error occurred during signup');
    }
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
    <Emotion10ThemeProvider theme={theme}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <GlobalStyles />
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: '100vh',
            backgroundColor: theme.palette.background.default,
          }}
        >
          <Card sx={{ maxWidth: 400, width: '100%' }}>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
                <img src={'https://picsum.photos/100'} alt="Logo" style={{ borderRadius: '50%' }} />
              </Box>
              <Typography variant="h5" align="center" gutterBottom>
                KasuwanDauri
              </Typography>
              <Tabs value={tab} onChange={handleChange} centered>
                <Tab label="Sign Up" />
                <Tab label="Sign In" />
              </Tabs>
              {tab === 0 && (
                <Box component="form" onSubmit={doSignup} sx={{ mt: 2 }}>
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Username"
                    name="username"
                    value={signupData.username}
                    onChange={handleSignupChange}
                    autoComplete="username"
                    autoFocus
                  />
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Email"
                    name="email"
                    type="email"
                    value={signupData.email}
                    onChange={handleSignupChange}
                    autoComplete="email"
                  />
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Password"
                    type="password"
                    name="password"
                    value={signupData.password}
                    onChange={handleSignupChange}
                    autoComplete="current-password"
                  />
                  {loading ? (
                    <LinearProgress sx={{ width: '100%' }} />
                  ) : (
                    <Button
                      type="submit"
                      fullWidth
                      variant="contained"
                      color="primary"
                      sx={{ mt: 3, mb: 2 }}
                    >
                      Sign Up
                    </Button>
                  )}
                </Box>
              )}
              {tab === 1 && (
                <Box component="form" onSubmit={doLogin} sx={{ mt: 2 }}>
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Username"
                    name="username"
                    value={loginData.username}
                    onChange={handleLoginChange}
                    autoComplete="username"
                    autoFocus
                  />
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Password"
                    name="password"
                    type="password"
                    value={loginData.password}
                    onChange={handleLoginChange}
                    autoComplete="current-password"
                  />
                  {loading ? (
                    <LinearProgress sx={{ width: '100%' }} />
                  ) : (
                    <Button
                      type="submit"
                      fullWidth
                      variant="contained"
                      color="primary"
                      sx={{ mt: 3, mb: 2 }}
                    >
                      Sign In
                    </Button>
                  )}
                </Box>
              )}
            </CardContent>
            <Box
              sx={{ textAlign: 'center', py: 2, borderTop: '1px solid', borderColor: theme.palette.divider }}
            >
              <Typography variant="body2" color="text.secondary">
                © 2024 KasuwanDauri. All rights reserved.
              </Typography>
            </Box>
          </Card>
          <ToastContainer
            position="bottom-right"
            autoClose={3000}
            hideProgressBar={false}
            style={{ marginBottom: '30px' }}
          />
        </Box>
      </ThemeProvider>
    </Emotion10ThemeProvider>
  );
};

export default Auth;
