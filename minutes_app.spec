# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['minutes_app.py'],
    pathex=[],
    binaries=[
        ('/opt/homebrew/Cellar/ffmpeg/7.1/bin/ffmpeg', '.'), 
        ('/opt/homebrew/Cellar/ffmpeg/7.1/bin/ffprobe', '.')
    ],
    datas=[
        ('面接議事録テンプレート.docx', '.')
    ],
    hiddenimports=[
        'tkinter', 
        'google.generativeai', 
        'openpyxl', 
        'dotenv', 
        'docx'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='minutes_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

app = BUNDLE(
    exe,
    name='minutes_app.app',
    icon=None,
    bundle_identifier=None,
)
