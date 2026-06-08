import React from 'react';
import s from './ScoreBar.module.css';

export default function ScoreBar({ score }) {
  const color =
    score >= 80 ? 'var(--accent)' :
    score >= 50 ? 'var(--warn)' : 'var(--danger)';

  const label =
    score >= 80 ? 'Excellent' :
    score >= 60 ? 'Good' :
    score >= 40 ? 'Needs Work' : 'Critical';

  return (
    <div className={s.wrap}>
      <div className={s.header}>
        <span className={s.title}>Quality Score</span>
        <span className={s.score} style={{ color }}>{score}<span className={s.max}>/100</span></span>
      </div>
      <div className={s.track}>
        <div
          className={s.fill}
          style={{ width: `${score}%`, background: color }}
        />
      </div>
      <span className={s.label} style={{ color }}>{label}</span>
    </div>
  );
}
