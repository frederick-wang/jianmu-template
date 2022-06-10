import { API } from '../../scripts/electron/preload'

export {}

declare global {
  interface Window {
    api: API
  }
}
