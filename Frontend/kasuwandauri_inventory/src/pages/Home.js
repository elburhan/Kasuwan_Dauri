// src/pages/Home.js
import React from 'react';
import { getUser } from '../utils/Helper';

const Home = () => {
  const user = getUser();
  return <h1>Home Page, Hi, {user.username}</h1>;
};

export default Home;
