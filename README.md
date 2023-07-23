# euanka-rasa


### 安装

安装 conda python3.9

安装 rasa >3.4


```
#
# To activate this environment, use
#
#     $ conda activate rasa
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```


安装rasa
pip install rasa==3.4.6 -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/

rasa init

一直确认即可


安装spacy
pip install spacy==3.4.4 -i https://pypi.tuna.tsinghua.edu.cn/simple

下载spacy对应的模型

wget https://github.com/explosion/spacy-models/releases/download/zh_core_web_md-3.4.0/zh_core_web_md-3.4.0-py3-none-any.whl

安装作为依赖
pip install zh_core_web_md-3.4.0-py3-none-any.whl


### 训练

训练
rasa train

仅启动rasa nlu服务，指定使用的模型
rasa run --enable-api -m models/20230325-165522-metallic-inertia.tar.gz

curl localhost:5005/model/parse -d '{"text":"hello"}'

curl localhost:5005/model/parse -d '{"text":"今天深圳天气"}'


###  rasa 启动
语义
rasa run -vv --cors "*"

actions服务
rasa run actions

