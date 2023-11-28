// src/Register.tsx

import React, { useState, ChangeEvent, FormEvent } from 'react';
import './Register.css';
import axios from 'axios';

interface FormData {
    email: string;
    password1: string;
    password2: string;
}

const Register: React.FC = () => {
    const [formData, setFormData] = useState<FormData>({
        email: '',
        password1: '',
        password2: ''
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
            const response = await axios.post('http://localhost:8000/rest-auth/registration/', formData);
            console.log('Registration successful:', response.data);
        } catch (error) {
            // @ts-ignore: Unreachable code error
            console.error('Error during registration:', error.response?.data);
        }
    };


    return (
        <div className="Register">
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <div className='user-box'>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                    <label>Email</label>
                </div>
                <div className='user-box'>
                    <input type="password" name="password1" value={formData.password1} onChange={handleChange} required/>
                    <label>Password</label>
                </div>
                <div className='user-box'>
                    <input type="password" name="password2" value={formData.password2} onChange={handleChange} required/>
                    <label>Confirm Password</label>
                </div>
                <div className="register-button">
                    <button type="submit" className="register-button-button">Register</button>
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


export default Register;
