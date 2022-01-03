mkdir /usr/src/app/data/
wget -O /usr/src/app/data/Ano-2021.csv.zip https://www.camara.leg.br/cotas/Ano-2021.csv.zip && unzip '/usr/src/app/data/Ano-2021.csv.zip' -d /usr/src/app/data/ && rm /usr/src/app/data/Ano-2021.csv.zip || true;

python main.py --temp_location=gs://gcs-3d23620d33571f6fbbe3f1d46e07652b/temp --staging_location=gs://gcs-3d23620d33571f6fbbe3f1d46e07652b/stage