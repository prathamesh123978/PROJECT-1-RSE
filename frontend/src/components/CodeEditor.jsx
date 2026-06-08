import React from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { javascript } from '@codemirror/lang-javascript';
import { oneDark } from '@codemirror/theme-one-dark';
import s from './CodeEditor.module.css';

const LANG_EXTENSIONS = {
  Python:     [python()],
  JavaScript: [javascript()],
  TypeScript: [javascript({ typescript: true })],
};

export default function CodeEditor({ value, onChange, language = 'Python' }) {
  const extensions = LANG_EXTENSIONS[language] || [python()];

  return (
    <div className={s.wrap}>
      <CodeMirror
        value={value}
        height="360px"
        theme={oneDark}
        extensions={extensions}
        onChange={onChange}
        basicSetup={{
          lineNumbers: true,
          highlightActiveLineGutter: true,
          foldGutter: true,
          autocompletion: true,
        }}
        style={{ fontSize: '13px' }}
      />
    </div>
  );
}
