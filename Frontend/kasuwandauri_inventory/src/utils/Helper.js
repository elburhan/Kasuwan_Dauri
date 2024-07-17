import {jwtDecode} from "jwt-decode"; // Correct import for default export

// Check if the user is authenticated by verifying the token
export const isAuthenticated = () => {
  const token = localStorage.getItem('token');
  if (!token) {
    return false; // User is not authenticated if token is not present
  }

  try {
    const decodedToken = jwtDecode(token);
    const currentTime = Date.now() / 1000;

    if (decodedToken.exp < currentTime) { // Added missing parenthesis
      localStorage.removeItem('token'); // Remove token if expired
      return false; // Token is expired
    }

    return true; // Token is valid
  } catch (error) {
    console.error('Error decoding token:', error);
    return false; // Return false on error
  }
};

// Get the user information from the token
export const getUser = () => {
  const token = localStorage.getItem('token');
  if (token) {
    try {
      const decodedToken = jwtDecode(token);
      return decodedToken; // Return decoded user information from token
    } catch (error) {
      console.error('Error decoding token:', error);
      return null; // Return null on error
    }
  }

  return null; // Return null if token is not present
};
