FROM --platform=linux/amd64 python:3.11-bookworm

ENV DISPLAY=:99
ENV CHROME_VER 114.0.5735.90-1
ENV CHROMEDRV_VER 114.0.5735.90
ENV CHROMEDRV_DIR /chromedriver

WORKDIR /root

RUN apt-get update -y \
 && apt-get install -y wget xvfb unzip vim \
 && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
 && apt-get update -y \
 && wget --no-verbose -O /tmp/chr.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VER}_amd64.deb \
 && apt install -y /tmp/chr.deb \
 && rm /tmp/chr.deb \
 && mkdir $CHROMEDRV_DIR \
 && wget -q --continue -P $CHROMEDRV_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRV_VER/chromedriver_linux64.zip" \
 && unzip $CHROMEDRV_DIR/chromedriver* -d $CHROMEDRV_DIR \
 && echo "alias ll='ls -la'" >> /root/.bashrc \
 && python -m pip install --upgrade pip \
 && python -m pip install --upgrade setuptools \
 && python -m pip install --upgrade selenium undetected-chromedriver

COPY test.py /root/test.py

ENV PATH $CHROMEDRV_DIR:$PATH

CMD ["python", "/root/test.py"]
