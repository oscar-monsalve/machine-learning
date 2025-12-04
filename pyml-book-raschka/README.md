# Virtual environment

According to the book's recommended virtual environment, [uv](https://docs.astral.sh/uv/) was used to create the venv as follows:

- Create a virtual environment. The code in the book used Python 3.9:

```shell
uv venv --python 3.9 .venv
```
- Activate the virtual environment:
```shell
source .venv/bin/activate
```
- Install packages according with the versions recommended by the book. These versions do not work for Python >3.13, so Python 3.9 has to be used:
```shell
uv pip install -r requirements.txt
```
- Check the packages' versions:
```shell
uv pip list
```
