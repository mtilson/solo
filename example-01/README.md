### 1-st working version

* How to build

```
$ docker build -t local/selenium-in-docker:01 .
```

* How to run

```
$ docker run --rm -ti --name test_example_com local/selenium-in-docker:01

Answer is: Example Domain
Should be: Example Domain
```
