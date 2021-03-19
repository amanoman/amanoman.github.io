import matplotlib
print(matplotlib.matplotlib_fname())  # 設定ファイルを表示（matplotlibrcは後で作ります）
print(matplotlib.rcParams['font.family'])  # 現在使用しているフォントを表示
print(matplotlib.get_configdir())  # 設定ディレクトリを表示
print(matplotlib.get_cachedir())  # キャッシュディレクトリを表示
