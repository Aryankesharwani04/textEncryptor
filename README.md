# Text Encryption and Decryption Project

## **Overview**
The Text Encryption and Decryption project provides a secure way to encode and decode messages using popular encryption techniques such as substitution ciphers, transposition ciphers, and a combination of both (complex cipher). It allows users to encrypt their messages to ensure confidentiality and decrypt them when needed. The project is designed with a React frontend and a Flask backend, making it a great example of integrating modern frameworks for web application development.

## **Importance of the Project**
1. **Data Security**: In today’s world, protecting sensitive information is crucial. This project demonstrates how to implement basic encryption techniques to ensure data security.
2. **Practical Learning**: It provides hands-on experience with encryption algorithms, showcasing their real-world applications.
3. **Full-Stack Development**: The project is an excellent opportunity to explore the integration of frontend and backend technologies.
4. **Customizability**: By understanding the implementation of encryption algorithms, users can extend the project to incorporate advanced cryptographic methods.

---

## **Backend Implementation**
The backend is developed using the Flask framework, a lightweight and easy-to-use Python framework for web development. Key features of the backend include:

1. **Flask Framework**:
    - Handles HTTP requests from the frontend and processes encryption/decryption logic.
    - Routes such as `/encrypt` and `/decrypt` are defined to process POST requests.

2. **Flask-CORS Integration**:
    - Allows cross-origin resource sharing, enabling the React frontend (running on a different port) to communicate with the Flask backend.
    - Configured specifically to allow requests from `http://localhost:5173` (the frontend's development server).

3. **Encryption Logic**:
    - Implements substitution ciphers, transposition ciphers, and complex ciphers for encoding and decoding messages.
    - Separate functions are defined for each type of cipher to ensure modularity.

---

## **Frontend Implementation**
The frontend is built with React, using Vite for its fast development environment. It features a user-friendly interface that:

1. **Takes User Input**:
    - Users can enter text, encryption keys, and select the type of encryption.
2. **Displays Results**:
    - Shows the encrypted and decrypted results on the same page for convenience.

### Key Features of React Framework in the Project
- **Component-Based Architecture**: The entire frontend is divided into reusable components, making the code modular and easy to maintain.
- **State Management**: The use of React's `useState` hooks ensures efficient handling of user input and results.

### Connection to Backend
The frontend communicates with the backend using `fetch` API calls to endpoints such as `/encrypt` and `/decrypt`. These API calls send JSON payloads containing the text, key, and cipher type to the backend and display the processed results.

---

## **Proxy Configuration in Vite**
To ensure seamless communication between the frontend and backend during development, a proxy is configured in `vite.config.js`. This eliminates the need to hardcode the backend URL in API calls.

### Advantages of Using a Proxy
- **Simplified API Calls**: Avoids CORS issues by routing requests through the Vite development server.
- **Dynamic Backend URL**: Allows easier configuration when deploying the app.

---

## **How the Application Works**
1. **Frontend Input**:
    - Users input text, key, and select the encryption mode.
    - The `Encrypt` button sends data to the `/encrypt` endpoint of the backend.
    - The `Decrypt` button sends data to the `/decrypt` endpoint.

2. **Backend Processing**:
    - The Flask backend processes the request and applies the selected encryption/decryption algorithm.

3. **Result Display**:
    - The frontend receives the response and displays the result to the user.

---

## **Conclusion**
This project highlights the integration of Flask and React to create a fully functional text encryption and decryption tool. By leveraging Flask for backend logic and React for a responsive frontend, the project demonstrates the power of modern web development frameworks. The use of a Vite proxy further streamlines development, making the app robust and easy to deploy.

