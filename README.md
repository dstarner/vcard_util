# Python vCard Utility

A utility library for working with [the **Virtual Contact File** (abbreviated as _vCard_) format](https://en.wikipedia.org/wiki/VCard) and contact books in general. It is tested to work with Python 3.11 and above.

## Early Development

This code is a cleaner, more module implementation of code that has been included in a personal side project, so parts of it may be very experimental and buggy. If you notice anything amiss, please file an [Issue](../../issues). Pull Requests are also greatly appreciated, although I have no set schedule to approve anything at the moment, as I anticipate being the only one using this for a while. 

## Local Development

After [cloning this repository to your local machine](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository), you will need to configure `poetry` and your VSCode editor to work smoothly.

1. Ensure you have `poetry` available in your shell. It might be as easy as installing it via `pip`.
   ```console
   pip install poetry
   ```
2. Create a virtual environment managed by `poetry` by running the following _inside_ the cloned repository.
   ```console
   poetry shell
   ```
3. Copy the VSCode settings example file to the local path, and update the `python.defaultInterpreterPath` value to the full path of your `poetry`-created virtual environment. It is already mostly templated out for you, if you use the default `poetry` settings.
   ```console
   cp .vscode/settings.example.json .vscode/settings.json
   ```
4. Install the dependencies
   ```console
   poetry install
   ```
