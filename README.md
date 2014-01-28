マルチプラットフォーム用のパッケージを作るサンプルスクリプト
============================================================

備忘のために libmsgpack を題材にして、rpm と windows 用のバイナリを作るスクリプトを残しておく。

Windowsの場合のビルド
---------------------

Gradle と Visual Studio Express を使う:

    setlocal enableDelayedExpansion
    call "%MSSdk%"\bin\SetEnv.cmd /Release /x86
    cd windows
    call gradle clean dist

RHELの場合のビルド
------------------

make と rpmbuild を使う:

    cd rpm
    make clean build
