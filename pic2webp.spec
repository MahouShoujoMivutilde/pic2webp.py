# -*- mode: python -*-

block_cipher = None

a = Analysis(['pic2webp.py'],
             pathex = [
              'pic2webp.py', 
              r'C:\Program Files (x86)\Windows Kits\10\Redist\ucrt\DLLs\x64'
              ],
             binaries = [],
             datas = [],
             hiddenimports = [],
             hookspath = [],
             runtime_hooks = [],
             excludes = [],
             win_no_prefer_redirects = False,
             win_private_assemblies = False,
             cipher = block_cipher)

pyz = PYZ(a.pure, a.zipped_data, cipher = block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name = 'pic2webp',
          debug = False,
          strip = False,
          upx = False,
          runtime_tmpdir = None,
          console = True)