{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixos-22.11.tar.gz") {} }:
pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (ps: [
      ps.flask
      ps.qrcode
      ps.numpy
      ps.matplotlib
    ]))

    pkgs.curl
    pkgs.vim
    pkgs.sqlite
    pkgs.tmux
    pkgs.tree
  ];

  shellHook = ''
    export FLASK_APP=main.py
    export FLASK_ENV=development
    export FLASK_RUN_PORT=5000
    '';
}
