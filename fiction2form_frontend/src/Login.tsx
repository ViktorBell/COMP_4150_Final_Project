// src/Login.tsx

import React, { useState, ChangeEvent, FormEvent } from 'react';
import './Login.css';
import axios from 'axios';

interface FormData {
    email: string;
    password: string;
}

const Login: React.FC = () => {
    const [formData, setFormData] = useState<FormData>({
        email: '',
        password: '',
    });

    const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSubmit = async (e: FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://localhost:8000/rest-auth/login/', formData);
            console.log('Login successful:', response.data);
        } catch (error) {
            // @ts-ignore: Unreachable code error
            console.error('Error during Login:', error.response?.data);
        }
    };


    return (
        <div className="Login">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div className='user-box'>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                    <label>Email</label>
                </div>
                <div className='user-box'>
                    <input type="password" name="password" value={formData.password} onChange={handleChange} required/>
                    <label>Password</label>
                </div>
                <div className="login-button">
                    <button type="submit" className="login-button-button">Login</button>
                </div>
            </form>
        </div>
    );

    /*
    return (
        <div className="login-box">
            <h2>Login</h2>
            <form>
                <div className="user-box">
                    <input type="text" name="" required/>
                        <label>Username</label>
                </div>
                <div className="user-box">
                    <input type="password" name="" required/>
                        <label>Password</label>
                </div>
                <a href="#">
                    <span></span>
                    <span></span>
                    <span></span>
                    <span></span>
                    Submit
                </a>
            </form>
        </div>
    ) */
};


export default Login;
