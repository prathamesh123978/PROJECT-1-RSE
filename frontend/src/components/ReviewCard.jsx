import React, { useState } from 'react';
import s from './ReviewCard.module.css';

const ICONS = {
  bug:      { icon: '🐛', color: 'var(--danger)',  label: 'Bug'      },
  smell:    { icon: '💨', color: 'var(--warn)',    label: 'Code Smell' },
  security: { icon: '🔒', color: 'var(--accent2)', label: 'Security' },
  perf:     { icon: '⚡', color: 'var(--info)',    label: 'Performance' },
};

const SEV_COLOR = {
  high:   'var(--danger)',
  medium: 'var(--warn)',
  low:    'var(--accent)',
};

export default function ReviewCard({ type, item }) {
  const [open, setOpen] = useState(false);
  const meta = ICONS[type] || ICONS.bug;

  const fix = item.fix || item.suggestion;
  const desc = item.description;

  return (
    <div className={s.card} style={{ borderLeftColor: meta.color }}>
      <div className={s.header} onClick={() => setOpen(o => !o)}>
        <div className={s.left}>
          <span className={s.icon}>{meta.icon}</span>
          <div>
            <div className={s.desc}>{desc}</div>
            <div className={s.meta}>
              <span className={s.badge} style={{ color: meta.color, borderColor: meta.color }}>
                {meta.label}
              </span>
              {item.severity && (
                <span className={s.severity} style={{ color: SEV_COLOR[item.severity] || 'var(--muted)' }}>
                  {item.severity.toUpperCase()}
                </span>
              )}
              {item.line && (
                <span className={s.line}>Line {item.line}</span>
              )}
            </div>
          </div>
        </div>
        <span className={s.chevron} style={{ transform: open ? 'rotate(180deg)' : 'rotate(0)' }}>▾</span>
      </div>

      {open && fix && (
        <div className={s.fix}>
          <div className={s.fixLabel}>Suggested Fix</div>
          <pre className={s.code}>{fix}</pre>
        </div>
      )}
    </div>
  );
}
