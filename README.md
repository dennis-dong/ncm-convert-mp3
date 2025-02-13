> python 版本推荐 3.8 及以上

## 1.把根文件夹放在音乐文件目录

```
轻舟-张杰.ncm
无名的人-毛不易.ncm
ncm-convert-mp3
```

## 2.执行下面脚本创建虚拟环境

```
cd ncm-convert-mp3

pip install -r -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

virtualenv venv
```

## 激活虚拟环境并运行

```
venv\Script\active

python run.py
```
