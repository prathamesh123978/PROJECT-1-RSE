import React from 'react';
import { NavLink } from 'react-router-dom';
import styled from './Navbar.module.css';

export default function Navbar() {
  return (
    <nav className={styled.nav}>
      <div className={styled.logo}>
        <span className={styled.bracket}>&lt;</span>
        CodeScan
        <span className={styled.accent}>AI</span>
        <span className={styled.bracket}>/&gt;</span>
      </div>
      <div className={styled.links}>
        <NavLink to="/" className={({ isActive }) => isActive ? `${styled.link} ${styled.active}` : styled.link}>
          Review
        </NavLink>
        <NavLink to="/history" className={({ isActive }) => isActive ? `${styled.link} ${styled.active}` : styled.link}>
          History
        </NavLink>
      </div>
    </nav>
  );
}
