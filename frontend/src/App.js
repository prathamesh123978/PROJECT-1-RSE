import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Navbar from './components/Navbar';
import ReviewPage from './pages/ReviewPage';
import Dashboard from './pages/Dashboard';

export default function App() {
  return (
    <>
      <Toaster
        position="top-right"
        toastOptions={{
          style: {
            background: '#1a1a24',
            color: '#e8e8f0',
            border: '1px solid #2a2a3a',
            fontFamily: "'Space Mono', monospace",
            fontSize: '13px',
          },
        }}
      />
      <Navbar />
      <Routes>
        <Route path="/" element={<ReviewPage />} />
        <Route path="/history" element={<Dashboard />} />
      </Routes>
    </>
  );
}
