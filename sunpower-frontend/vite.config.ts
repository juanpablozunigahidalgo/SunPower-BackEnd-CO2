import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Vite 5 config, no rolldown, works with Node 20.9
export default defineConfig({
  plugins: [react()],
  server: {
    strictPort: true,
    port: 5173,
  }
})
