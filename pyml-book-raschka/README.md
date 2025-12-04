# Virtual environment

According to the recommended venv recommended by the book, [uv](https://docs.astral.sh/uv/) was used to create the venv as follows:

- Create the virtual environment in book's directory (```pyml-book-raschka```):

```shell
uv venv --python 3.9 .venv
```
- Activate the virtual environment:
```shell
source .venv/bin/activate
```
- Install packages according with the versions recommended by the book:
```shell
uv pip install -r requirements.txt
```
- Check the packages' versions:
```shell
uv pip list
```
