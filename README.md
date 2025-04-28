gRPC Typing Stubs for Python
============================

> [!WARNING]
>
> **2025-04-28: The end of the line for `grpc-stubs`**.
>
> My involvement with grpc ceased around 2019, and my knowledge of the minutiae faded
> with each passing year. As a consequence, this this project has been archived, but
> development will continue at
> [typeshed](https://github.com/python/typeshed/tree/main/stubs/grpcio). Thank you to
> the folks who helped [prepare the code for
> merging](https://github.com/python/typeshed/pull/11204).

This is a PEP-561-compliant stub-only package which provides type information of
[gRPC](https://grpc.io>).

Install using pip:

    pip install grpc-stubs

Tests (courtesy of [pytest-mypy-plugins](https://github.com/typeddjango/pytest-mypy-plugins>):

    pip install -r requirements-dev.txt
    ./tools.sh test


## Python Support

grpc-stubs is tested with 3.7 or later, but ideally it should support Python 3.6 as
grpc still supports this. Python 3.6 had to be disabled in the tests due to
various cascading fiascos and a lack of time to contend with them. Feel free
to submit a PR if you'd like to see it returned, or open issues. Ensure that
you supply an MRE as per the contributing guidelines below.

