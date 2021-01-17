## list_gh_contributions

Script to list all of the repositories you've contributed to on Github. Includes your own repositories and any repositories you've contributed to (a commit, PR or issue)

## Installation

Requires `python3.6+`

To install with pip, run:

    pip install git+https://github.com/seanbreckenridge/list_gh_contributions

---

## Usage

Go to Github Developer Settings and create a 'Personal Access Token' (https://github.com/settings/tokens).

The only scopes this requires is `repo`

Put the generated token in a text file on the first line

Example:

```
python3 -m list_gh_contributions --github_token ./token.txt --to-csv > repos.csv
```

Usage:

```
Usage: list_gh_contributions [OPTIONS]

  Prints results to STDOUT

Options:
  --github-token PATH  Text file which contains your Github token  [required]
  --to-csv             Convert output to CSV instead
  --help               Show this message and exit.
```

---

## Example

```
$ python3 -m list_gh_contributions --github-token ./token.txt --to-csv | head
"name/owner","url","licenseInfo","updatedAt"
"seanbreckenridge/mal-id-cache","https://github.com/seanbreckenridge/mal-id-cache","MIT License","2021-01-16T16:51:38Z"
"seanbreckenridge/exobrain","https://github.com/seanbreckenridge/exobrain","Other","2021-01-15T10:42:04Z"
"seanbreckenridge/HPI","https://github.com/seanbreckenridge/HPI","MIT License","2021-01-15T10:41:56Z"
"seanbreckenridge/mint","https://github.com/seanbreckenridge/mint","MIT License","2021-01-14T23:21:27Z"
"seanbreckenridge/dotfiles","https://github.com/seanbreckenridge/dotfiles","","2021-01-12T03:43:22Z"
"seanbreckenridge/plaintext-playlist","https://github.com/seanbreckenridge/plaintext-playlist","MIT License","2021-01-07T07:41:29Z"
"seanbreckenridge/chomp","https://github.com/seanbreckenridge/chomp","","2021-01-07T04:11:13Z"
"seanbreckenridge/projects","https://github.com/seanbreckenridge/projects","MIT License","2021-01-07T01:57:09Z"
"seanbreckenridge/newest","https://github.com/seanbreckenridge/newest","","2021-01-07T01:35:20Z"
```
