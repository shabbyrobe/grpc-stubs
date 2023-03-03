## Description of change

## Minimum Reproducible Example

> Pull requests of any significance *will not be accepted* without minimum reproducible examples.
> If your contribution is small enough (a few lines tops), a typing test might be enough, but an MRE might still
> be requested. If in doubt, presume an MRE will be required.
>
> Pull requests where an MRE is requested but not supplied will be closed.
>
> "Reproducible" means you have given me enough materials to exercise runnable code that 
> demonstrates your change, on my local machine, with a minimum of fuss.
> 
> Gists, links to other repositories, or typing tests are not acceptable as an MRE.
> 
> If an MRE is needed (it probably is), the following must be provided, at a minimum, in
> separate `<details>` blocks, using as few files as possible (templates are provided below): 
>
> - One or more python files containing reproducing code.
> - Full set of shell commands (POSIX shell or bash only) required to create a venv, install
>   dependencies, and generate proto.
>
> Please see README.md for the rationale for why this is needed.

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

## Checklist:

- [ ] I have verified my MRE is sufficient to demonstrate the issue and solution by attempting to execute it myself
  - [ ] **OR** I believe my contribution is minor enough that a typing test is sufficient.
- [ ] I have added tests to `typesafety/test_grpc.yml` for all APIs added or changed by this PR
- [ ] I have removed any code generation notices from anything seeded using `mypy-protobuf`.
