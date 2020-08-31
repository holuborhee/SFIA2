cd service1
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..

cd service2
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..

cd service3
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..

cd service4
pip3 install -r requirements.txt
python3 -m pytest --cov application --cov-report term-missing
cd ..