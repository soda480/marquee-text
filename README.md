# marquee-text
[![complexity](https://img.shields.io/badge/complexity-Simple:%204-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)
[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)
[![python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-teal)](https://www.python.org/downloads/)

A simple text marquee.

### Installation
```bash
pip install marquee_text
```

#### [example1](https://github.com/soda480/marquee_text/blob/main/examples/example1.py)

<details><summary>Code</summary>

```Python
```

</details>

![example1](https://raw.githubusercontent.com/soda480/marquee_text/main/docs/images/example1.gif)

### Development

Clone the repository and ensure the latest version of Docker is installed on your development server.

Build the Docker image:
```sh
docker image build \
-t \
marquee_text:latest .
```

Run the Docker container:
```sh
docker container run \
--rm \
-it \
-v $PWD:/code \
marquee_text:latest \
bash
```

Execute the build:
```sh
pyb -X
```
