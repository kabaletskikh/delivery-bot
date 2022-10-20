FROM python:3.8-buster



RUN apt-get install git
RUN git clone github.com/kabaletskikh/delivery-bot.git
RUN pip install --no-cache-dir -r delivery-bot/src/req.txt



CMD [ "python", "./delivery-bot/src/req.txt" ]