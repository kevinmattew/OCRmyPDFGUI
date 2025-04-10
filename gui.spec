# -*- mode: python ; coding: utf-8 -*-
import platform
from PyInstaller.utils.hooks import collect_data_files

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
        # 包含 SVG 图标文件
        ('docs/images/logo-square-256.svg', '.'),
        # PyQt6 翻译文件会通过 collect_data_files 自动收集
        *collect_data_files('PyQt6', includes=['**/translations/*'])
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
if platform.system() == 'Darwin':
    app = BUNDLE(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        name='OCRmyPDF-GUI.app',
        icon='OCRmyPDF.icns',  # 替换为生成的 .icns 文件
        bundle_identifier='org.ocrmypdf.gui',
        info_plist={
            'NSHighResolutionCapable': 'True',
            'LSBackgroundOnly': 'False',
            'NSRequiresAquaSystemAppearance': 'False',
        },
    )
