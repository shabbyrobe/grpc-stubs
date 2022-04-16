## Description of issue


## Minimum Reproducible Example

> Pull requests will not be accepted without minimum reproducible examples. "Reproducible" in this case
> means the following is provided, in separate `<details>` blocks, using as few files as possible. Gists
> and links to other repositories are not acceptable as an MRE. Pull requests without an MRE will be
> immediately closed.
>
> - One or more python files containing reproducing code.
> - Full set of shell commands (POSIX shell or bash only) required to create a venv, install
>   dependencies, and generate proto.
>
> This is necessary due to the large number of PRs that have been missing tests or examples, which
> causes knock-on effects for all users.

<details>
<summary>main.py</summary>

```py
# Full python code to reproduce
if __name__ == "__main__":
    ...
```

</details>

<details>
<summary>run.sh</summary>

```sh
#!/usr/bin/env bash
set -o errexit -o nounset -o pipefail
python -m venv venv
source ./venv/bin/activate
pip install $INSERT_DEPENDENCIES_HERE
python main.py
```

</details>
