マルチプラットフォーム用のパッケージを作るサンプルスクリプト
============================================================

libmsgpack を題材にして、rpm と windows 用のバイナリを作るサンプルスクリプト。

Windowsの場合のビルド
---------------------

    setlocal enableDelayedExpansion
    call "%MSSdk%"\bin\SetEnv.cmd /Release /x86
    cd windows
    call "%GRADLE_HOME%"\bin\gradle --info clean dist

RHELの場合のビルド
------------------

    cd rpm
    make clean build
