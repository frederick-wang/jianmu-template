const Path = require('path')
const vuePlugin = require('@vitejs/plugin-vue')
const { createHtmlPlugin } = require('vite-plugin-html')
const { productName, version } = require('../package.json')

const { defineConfig } = require('vite')

/**
 * https://vitejs.dev/config
 */
const config = defineConfig({
  root: Path.join(__dirname, '..', 'ui'),
  publicDir: 'public',
  server: {
    port: 8080
  },
  open: false,
  build: {
    outDir: Path.join(__dirname, '..', '.jianmu', 'ui'),
    emptyOutDir: true
  },
  plugins: [
    vuePlugin(),
    createHtmlPlugin({
      inject: {
        data: {
          title: `${productName} ${version}`
        }
      }
    })
  ],
  resolve: {
    alias: {
      '@': Path.join(__dirname, '..', 'ui')
    }
  }
})

module.exports = config
