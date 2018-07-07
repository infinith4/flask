# flask
https://qiita.com/t2y/items/2a3eb58103e85d8064b6

## 環境を調べる

conda info -e

## 仮想環境を作る

conda create -n py36 python=3.6 anaconda

## 仮想環境を有効・無効にする

To activate this environment, use:
> source activate py36

To deactivate an active environment, use:
> source deactivate

## 仮想環境のpythonのVersionが2.7になってしまったら

仮想環境内で

conda install python=3.6

https://qiita.com/msrks/items/c57e0168fb89f160d488