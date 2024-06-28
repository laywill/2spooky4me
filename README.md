# 2spooky4me

Solution to a short programming puzzle: generate variants of the notable meme phrase "2spooky4me".

## Problem

Lovingly set by [@ACascarino](https://github.com/ACascarino) based on a StackOverflow post.

2spooky4me is a universal truth, but notable variations exist e.g. 3spooky5me.

Some people just can't handle that much spook, others are spook junkies, and we must cater for them as well.

Your task is to take an arbitrary string, e.g. `2spooky4me` or `1this2is3a4meme` and an operation, expressed as a string e.g. `*10`, `/2`, or `^3` and produce a string output applying the operation to your string, e.g. (`2spooky4me`, `*5`) -> `10spooky20me`

- All numbers are integers, so truncate: `3 / 2 = 1`.
- Your input string may contain no numbers.
- Your input string may contain no letters.
- Acceptable operations are `+`, `-`, `*`, `/`, and `^` (power).
- Your output may be negative, although no inputs will be.

Shortest answer wins one prize, most readable answer wins another, most elegant (subjective, tends to mean "short and readable") wins grand prize.


## Setup and Use

### Python Version

This has been developed using Python 3.11

### Create a virtual environment

On MacOS and Linux:

```bash
python3 -m venv venv
```

On Windows:

```powershell
python -m venv venv
```

### Activate virtual environment

On MacOS and Linux:

```bash
source venv/bin/activate
```

On Windows:

```powershell
.\venv\Scripts\activate
```

### Install packages from requirements

Tell pip to install all of the packages in this file using the -r flag:

```bash
pip install -r requirements.txt
```

## Running Scripts

Spooky_solver assumes you are running  from the root of the repository.
Script takes exactly two  parameters, and are invoked directly e.g.:

```bash
python ./spooky_solver.py 2spooky4me +69
```

## Tests

Install the dependencies

```bash
pip install pytest
```

Run the tests

```bash
pytest
```

Run the tests with individual test results

```bash
pytest -v
```
