import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
    plugins: [react()],
    root: '.',
    resolve: {
        alias: {
            shared: path.resolve(__dirname, '../../libs/shared')
        }
    },
    server: {
        port: 3000,
    },
    build: {
        outDir: 'dist'
    }
})