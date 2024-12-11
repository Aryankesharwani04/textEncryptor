import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/encrypt': 'http://127.0.0.1:5000',
      '/decrypt': 'http://127.0.0.1:5000',
    },
  },
});
