# Inspire Candidate Exercise

At Inspire, we care about hiring talented people, because we all rely on each other on a regular basis. This exercise isn't meant to be some exhaustive thing - you may find it very easy, or you may have to learn new things to finish it - but the point is to act as a sanity check of your ability to work with Python in an HTTP context. If you have an applicable prior project, you can share the source for that, instead of doing this exercise. But either way, we don't want to eat up your day, we just want to confirm that you can do the stuff that we do for a living!

### The Goal

We care a lot about testing, so we've provided you with the test file `tests/test_integration.py`. You can run it with the `pytest` command.

When all tests pass, you've finished the exercise! The tests are written as _documentation_ of what features you need to add, so please read the test source.

When your exercise is complete, wrap up this directory in a zip file and send your work over to us.

### The Playing Field

So what are you even working on here? Well, you're making changes to `app.py` to get it to pass the tests. This file contains:

1. A very simple webserver using the [BottlePy](https://bottlepy.org/docs/dev/api.html) microframework, and
2. An in-memory sqlite database, with a `wombat` table that has a handful of records.

Your goal is to add some endpoints to the webserver, which interact with the database. Read the tests for more detail.

### Setting Up

You don't need to install any system libraries to run or test the code. We provide infrastructure for `venv`:

```bash
# If you don't have python3.6:
python -m pip install virtualenv # augment with --user or sudo to taste
virtualenv --python=python3.6 .venv

# If you do have python3.6:
python3 -m venv .venv

# Either way, we can now....
source .venv/bin/activate
pip install -r requirements.txt # Feel free to add to requirements.txt if you need, but you shouldn't need to
```

Ah, but what if you're on Windows, or otherwise don't want to set up an environment on your host machine? Well, we also provide a `Dockerfile` for you.

```bash
docker build -t inspire-ce .
docker run -it inspire-ce sh # Start shell inside docker container

# Run tests and then drop into server process
docker run -it -p=8080:8080 inspire-ce
```

Be advised that if you're working with Docker, you'll probably need to rebuild the image repeatedly as part of your core feedback loop.

### Gotchas

Some things that you may find helpful while doing this exercise:

 * sqlite3.Row is great, but doesn't convert to a dict without a little help.
 * For security purposes, Bottle will treat `return {...}` as a JSON response, but not `return [...]`. This is to prevent [JSON hijacking](http://haacked.com/archive/2009/06/25/json-hijacking.aspx/).
 * `db.cursor().execute(sql, args)` _always_ takes args as a tuple (or other iterable), not an `*args` expansion.

### Contributing

To submit a completed exercise, put your repo in a .zip file and send it to us as part of your hiring communications.

To contribute improvements to the exercise itself, like the Dockerfile, feel free to make a PR here! We want this repo to test basic skills, but otherwise be as frictionless as possible. People should not fail out because their environment was a little funky or the instructions weren't clear.
