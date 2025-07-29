#!/bin/bash

APP_NAME="hmi-designer"
ICON_PATH="icons/app.ico"

pyinstaller \
    --name "$APP_NAME" \
    --onefile \
    --icon="$ICON_PATH" \
    --add-data "components/ui/*.ui:ui" \
    --add-data "configs:configs" \
    main.py
