#!/bin/bash

echo "清理 PyInstaller 构建缓存..."
rm -rf build dist __pycache__ *.spec components/__pycache__ *.spec core/__pycache__ *.spec /tmp/_MEI*
echo "✅ 清理完成"
