Install python if u haven't

IF Windows:

Initialize pip virutal env first you will need to install virtual env from pip

```
python -m pip install --user virtualenv
```

Create the virtual env using

```
python -m venv env
```

Activate virtual env

```
.\env\Scripts\activate
```

Install requirements.txt file

```
pip install -r requirements.txt
```

Run server using the following command

```
.\mysite\runserver.bat
```

Load data using the following command

```
.\mysite\loaddata.bat
```

IF Unix/MacOS:
Initialize pip virutal env first you will need to install virtual env from pip

```
python3 -m pip install --user virtualenv
```

Create the virtual env using

```
python3 -m venv env
```

Activate virtual env

```
source env/bin/activate
```

Install requirements.txt file

```
pip install -r requirements.txt
```

Run server using the following command

```
bash .\mysite\runserver.bash
```

Load data using the following command

```
bash .\mysite\loaddata.bash
```
