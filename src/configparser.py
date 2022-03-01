# data/config.iniファイルの読み込みテスト

import configparser
import os


def main(ini_path: str) -> None:
    config_ini = configparser.ConfigParser(os.environ, interpolation=configparser.ExtendedInterpolation())
    config_ini.read(ini_path, encoding='utf-8')
    dir = config_ini.get('DERIVATION', 'dir')
    print(dir)


if __name__ == '__main__':
    main('./config.ini')
