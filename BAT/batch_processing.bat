set d = '%3d'
for %%a in ("F:\zja\data\ma/train/*.y4m") do ffmpeg -i F:\zja\data\ma/train\%%~na.y4m -vsync 0 D:\zja\data\train\input\%%~na\%%d.bmp -y
pause
