FROM --platform=linux/amd64 python:3.11-bookworm

ENV DISPLAY=:99
ENV CHROMEDRIVER_VERSION 114.0.5735.90
ENV CHROME_VERSION 114.0.5735.90-1
ENV CHROMEDRIVER_DIR /chromedriver

WORKDIR /root

RUN apt-get update -y \
 && apt-get install -y wget xvfb unzip vim \
 && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
 && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
 && apt-get update -y \
 && wget --no-verbose -O /tmp/chrome.deb https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb \
 && apt install -y /tmp/chrome.deb \
 && rm /tmp/chrome.deb \
 && mkdir $CHROMEDRIVER_DIR \
 && wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" \
 && unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR \
 && python -m venv /root/ENVs/solo/dev/.venv \
 && /root/ENVs/solo/dev/.venv/bin/python -m pip install --upgrade pip \
 && /root/ENVs/solo/dev/.venv/bin/python -m pip install --upgrade setuptools \
 && /root/ENVs/solo/dev/.venv/bin/python -m pip install --upgrade selenium undetected-chromedriver \
 && echo "alias ll='ls -la'" >> /root/.bashrc

COPY test.py /root/ENVs/solo/test.py

ENV PATH $CHROMEDRIVER_DIR:$PATH

CMD ["/root/ENVs/solo/dev/.venv/bin/python", "/root/ENVs/solo/test.py"]
