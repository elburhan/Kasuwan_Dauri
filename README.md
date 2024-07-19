Kasuwan Dauri
Kasuwan Dauri is an e-commerce platform designed to help local Hausa artisans sell their materials online. The project includes several services such as Order Services, Product Services, User Services, and Inventory Services, all built using Django for the backend and React for the frontend.

Table of Contents
Project Description
Features
Technologies Used
Installation
Usage
API Endpoints
Contributing
License
Project Description
Kasuwan Dauri aims to provide a seamless platform for artisans to manage their products and orders. The application features a user authentication system, dynamic sidebar navigation, and a protected route mechanism to ensure secure access to various parts of the application.

Features
User Authentication:

Sign up and log in with JWT token-based authentication.
Protected routes to secure parts of the application.
User Management:

Retrieve and display user information from JWT token.
Sidebar Navigation:

Dynamic menu populated from API.
Expandable and collapsible menu items.
Order Management:

View and manage orders.
Product Management:

View and manage products.
Notifications:

Real-time toast notifications for user actions and system events.
Technologies Used
Frontend:

React
Material-UI
React Router
Redux
Axios
React-Toastify
Backend:

Django
Django REST Framework
Database:

PostgreSQL
API Documentation:

Swagger UI
Postman
Installation
Prerequisites
Node.js
npm or yarn
Python
Django
PostgreSQL
Backend Setup
Clone the repository:


git clone https://github.com/elburhan/kasuwan_dauri.git
cd kasuwan_dauri/backend
Create a virtual environment and activate it:


python -m venv venv
source venv/bin/activate
Install the required dependencies:


pip install -r requirements.txt
Run the Django development server:


python manage.py runserver
Frontend Setup
Navigate to the frontend directory:



cd ../frontend
Install the required dependencies:


npm install
Start the React development server:

bash
Copy code
npm start
Usage
Open your browser and go to http://localhost:3000 to view the application.

Use the signup feature to create a new user or log in with existing credentials.

Navigate through the application using the sidebar to manage products, orders, and user settings.

API Endpoints
Authentication
Login: POST /api/auth/login/
Signup: POST /api/auth/signup/
Sidebar
Fetch Sidebar Data: GET /api/getMenus/
Products
Get Products: GET /api/products/
Add Product: POST /api/products/add/
Orders
Get Orders: GET /api/orders/
Add Order: POST /api/orders/add/
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License - see the LICENSE file for details.