import { defineConfig, loadEnv } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath, URL } from 'node:url';

const toPort = (value, fallback) => {
  const parsed = Number.parseInt(value ?? '', 10);
  return Number.isInteger(parsed) && parsed > 0 ? parsed : fallback;
};

const toList = (value) =>
  value
    ?.split(',')
    .map((item) => item.trim())
    .filter(Boolean);

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), 'VITE_');

  const apiTarget = env.VITE_API_TARGET || 'http://127.0.0.1:8000';
  const allowedHosts = toList(env.VITE_ALLOWED_HOSTS);

  return {
    plugins: [react()],

    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },

    server: {
      host: env.VITE_DEV_HOST || '127.0.0.1',
      port: toPort(env.VITE_DEV_PORT, 5173),
      strictPort: true,
      allowedHosts,
      fs: {
        strict: true,
      },
      proxy: {
        '/api': {
          target: apiTarget,
          changeOrigin: true,
        },
      },
    },

    preview: {
      host: env.VITE_PREVIEW_HOST || '127.0.0.1',
      port: toPort(env.VITE_PREVIEW_PORT, 4173),
      strictPort: true,
      allowedHosts,
    },

    build: {
      outDir: 'dist',
      emptyOutDir: true,
      sourcemap: mode !== 'production',
    },
  };
});
