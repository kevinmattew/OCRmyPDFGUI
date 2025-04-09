# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 注意：PyInstaller 可能无法直接使用 SVG 图标
# 为了获得最佳跨平台兼容性，建议提供预转换的图标文件：
# - Windows: .ico 文件
# - macOS: .icns 文件
# 并将下面的 'icon' 参数替换为相应的文件路径

a = Analysis(
    ['gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        # 包含 PyQt6 的翻译文件
        ('/path/to/PyQt6/Qt6/translations', 'PyQt6/Qt6/translations'),
        # 包含 SVG 图标文件（虽然可能无法直接使用）
        ('docs/images/logo-square-256.svg', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='OCRmyPDF-GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # 设置为 False 以隐藏控制台窗口（仅适用于 Windows）
    icon='docs/images/logo-square-256.svg',  # 可能需要替换为 .ico 或 .icns 文件
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# 对于 macOS 应用捆绑包
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='OCRmyPDF-GUI',
)
