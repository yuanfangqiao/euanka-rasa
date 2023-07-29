FROM rasa/rasa:3.5.15
USER root


# COPY ./ /app/

# RUN rm -rf /app/.rasa && 
# rasa base config 
COPY ./data /app/data/
COPY ./config.yml /app/config.yml
COPY ./credentials.yml /app/credentials.yml
COPY ./domain.yml /app/domain.yml
COPY ./endpoints.yml /app/endpoints.yml
# spacy
COPY ./zh_core_web_md-3.4.0-py3-none-any.whl /app/zh_core_web_md-3.4.0-py3-none-any.whl

RUN  pip install spacy==3.4.4 -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install /app/zh_core_web_md-3.4.0-py3-none-any.whl  && rasa train

WORKDIR /app

CMD [ "run" ]
