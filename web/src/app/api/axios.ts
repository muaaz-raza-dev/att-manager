import axios from 'axios';
 
export const Axios = axios.create({
  baseURL: process.env.NEXT_APP_API_URL ,
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${localStorage.getItem('token') || ''}`,
  },
  
});

