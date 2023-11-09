# Building the JULES User Guide

The JULES documentation is contained in the doc project in this repository. This README describes how to build the JULES User Guide.

For first time users, please create the production environment to build the docs. From the top level of the repository run:

```
conda env create -f environment.yml
```

Activate the environment:

```
conda activate jules-user-guide
```

Build the documentation:

```
cd <path_to>/user_guide/doc
make html
```

View the documentation:
```
firefox build/html/index.html
```
