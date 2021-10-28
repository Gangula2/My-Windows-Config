# Quicklook

Installation:

    choco install quicklook

> One of the few features I missed from macOS is [Quick Look](https://en.wikipedia.org/wiki/Quick_Look). It allows users to peek into a file content in lightning speed by just pressing the <kbd>Space</kbd> key. Windows, on the other hand, does not have this handy feature ... until now!
> 
> I am aware that several alternatives are already available on the Internet (e.g. [WinQuickLook](https://github.com/shibayan/WinQuickLook) and [Seer](https://github.com/ccseer/Seer)). Despite these options, I still decided to craft another one by myself, because they are either not being actively developed, lack of variety, or ask for some :dollar:.
>
> ### Out-of-box support
> 
> - Your Desktop
> - File Explorer windows
> - Open and Save File dialogues (requires QuickLook MSI/ZIP versions, not Store version)
> - Everything (requires Everything being installed as a service)
> - [Files](https://www.microsoft.com/store/apps/9NGHP3DX8HDX)


## Plugins

### Download & Installation
1. Go to Release page of respective plugin repository and download the latest version.
2. Make sure that you have QuickLook running in the background. Go to your Download folder, and press <key>Spacebar</key> on the downloaded `.qlplugin` file.
3. Click the “Install” button in the popup window.
4. Restart QuickLook.

### OfficeViewer

Installation file: [./QuickLook.Plugin.OfficeViewer.qlplugin](./QuickLook.Plugin.OfficeViewer.qlplugin)

This plugin allows QuickLook to preview Office file formats, without the requirement of installing Office suite.
- [OfficeViewer - Release page](https://github.com/QL-Win/QuickLook.Plugin.OfficeViewer/releases)

### FontViewer

Installation file: [./QuickLook.Plugin.FontViewer.qlplugin](./QuickLook.Plugin.FontViewer.qlplugin)

A plugin for pre-viewing fonts in QuickLook: https://github.com/xupefei/QuickLook  
- [FontViewer - Release page](https://github.com/jeremyhart/QuickLook.Plugin.FontViewer/releases)

![fontviewer mockup](https://user-images.githubusercontent.com/2062475/47404316-5167c480-d7a9-11e8-8768-053ade6cddd3.jpg)

#### Supported Filetypes  
.OTF, .TTF

## All Plugins

All Avalilable plugins can be found here: https://github.com/QL-Win/QuickLook/wiki/Available-Plugins
