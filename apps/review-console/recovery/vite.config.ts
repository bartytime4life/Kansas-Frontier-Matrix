import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Dedicated loopback origin: no shared KFM API, database or operational service.
export default defineConfig({
  plugins: [react()],
  server: { host: '127.0.0.1', port: 5179, strictPort: true },
  preview: { host: '127.0.0.1', port: 4179, strictPort: true },
});
