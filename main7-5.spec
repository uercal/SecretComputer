# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main7-5.py'],
             pathex=['E:\\demo-2021\\SecretComputer'],
             binaries=[],
             datas=[('E:\\demo-2021\\SecretComputer\\setting.json','.'),('E:\\demo-2021\\SecretComputer\\pwd.ini','.'),
             ('E:\\demo-2021\\SecretComputer\\position-dan.txt','.'),('E:\\demo-2021\\SecretComputer\\position-shuang.txt','.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='main7-5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main7-5')
