#!/bin/bash

# Источник и назначение
SOURCE="/opt/database"
DEST="/opt/backup"

# Создаём папку назначения, если её нет
mkdir -p "$DEST"

# Копируем с сохранением прав и вложенности
cp -a "$SOURCE"/ "$DEST"/