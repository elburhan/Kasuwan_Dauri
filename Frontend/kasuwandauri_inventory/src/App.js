import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Layout from './layout/layout'; // Changed 'Layout' to 'layout'
import 'react-toastify/dist/ReactToastify.css';
import ProtectedRoute from './utils/ProtectedRoute';
import { ToastContainer } from 'react-toastify';
import Auth from './pages/Auth';
import { useState } from 'react';
import store from './redux/store/store';
import { useDispatch } from 'react-redux';
import { Provider } from 'react-redux';
import { fetchSidebar } from './redux/reducer/sidebardata';
import { useEffect,useReact } from 'react';




function App() {
  const 
  const sidebarItems = [
    { name: 'Home', link: '/home', icon: 'home' },
    { name: 'Products', link: '/products', icon: 'products' },
    { name: 'Orders', link: '/orders', icon: 'orders' },
    { name: 'Users', link: '/users', icon: 'users' },
    { name: 'Settings', link: '/settings', icon: 'settings' },
    { 
      name: 'Categories', 
      icon: 'categories', 
      children: [
        { name: 'All Categories', link: '/categories' },
        { name: 'Add Category', link: '/categories/add' }
      ]
    }
  ];

  return (
    <Router>
      <Routes>
        <Route path="/auth" element={<Auth />} />
        <Route path="/" element={<Layout sidebarList={sidebarItems} />}>
          <Route path="home" element={<ProtectedRoute element={<Home />} />} />
        </Route>
      </Routes>
      <ToastContainer
        position="bottom-right"
        autoClose={3000}
        hideProgressBar={false}
        style={{ marginBottom: '30px' }}
      />
    </Router>
  );
}

export default App;
