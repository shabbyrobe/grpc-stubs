gRPC Typing Stubs for Python
============================

This is a PEP-561-compliant stub-only package which provides type information of
`gRPC <https://grpc.io>`_.

Install using pip::

    pip install grpc-stubs


Tests (courtesy of `pytest-mypy-plugins <https://github.com/typeddjango/pytest-mypy-plugins>`_)::

    pip install -r requirements-dev.txt
    ./tools.sh test


## Contributing

Due to a series of incomplete PRs, starting from 2022-04-16, fairly strict issue and pull request
templates have been added. Minimum Reproducible Examples are now a hard requirement for pull requests,
and a soft requirement for issues. Incomplete PRs simply transfer the burden from the contributor to
the maintainer, and I simply don't have time to do the deep-dives required to rebuild MREs from scratch
when the issues from incomplete PRs inevitably crop up. 


## Calls for assistance

### Stubs for `aio` packages

Several attempts have been made to contribute stubs for the `aio` packages, but have had to be reverted.
A more substantive contribution would be very welcome, even if that is in the form of some MREs; I'm not
sufficiently involved with `grpc` on a daily basis any more to be able to confidently integrate it myself
without assistance.


## Other Very Useful Typed Python Stuff

- https://github.com/TypedDjango
- https://github.com/typeddjango/pytest-mypy-plugins
- https://github.com/typeddjango/awesome-python-stubs

