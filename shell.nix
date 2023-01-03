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
}
