import {
  contextBridge,
  ipcRenderer,
  OpenDialogOptions,
  OpenDialogReturnValue,
  SaveDialogOptions,
  SaveDialogReturnValue
} from 'electron'

interface PythonResponse<T = any> {
  error: number
  message: string
  data: T
}

const api = {
  minimize: () => ipcRenderer.send('minimize'),
  isMaximized: () => ipcRenderer.invoke('is-maximized') as Promise<boolean>,
  toggleMaximize: () => ipcRenderer.send('toggle-maximize'),
  close: () => ipcRenderer.send('close'),
  toggleDevtools: () => ipcRenderer.send('toggle-devtools'),
  reload: () => ipcRenderer.send('reload'),
  forceReload: () => ipcRenderer.send('force-reload'),
  quit: () => ipcRenderer.send('quit'),
  invokePython: <T = any>(method: string, ...args: any[]) =>
    ipcRenderer.invoke('invoke-python', method, ...args) as Promise<
      PythonResponse<T>
    >,
  showOpenDialog: (options: OpenDialogOptions) =>
    ipcRenderer.invoke(
      'show-open-dialog',
      options
    ) as Promise<OpenDialogReturnValue>,
  showSaveDialog: (options: SaveDialogOptions) =>
    ipcRenderer.invoke(
      'show-save-dialog',
      options
    ) as Promise<SaveDialogReturnValue>
}

type API = typeof api

contextBridge.exposeInMainWorld('api', api)

export { API, PythonResponse }
