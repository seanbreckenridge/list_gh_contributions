from pathlib import Path
from itertools import chain

import click
from gql import gql, Client  # type: ignore[import]

from . import JsonList
from .client import exhaust_github_query, construct_client
from .query import query_contributed_to, query_owned
from .printer import json_printer, csv_printer


@click.command(name="list_gh_contributions")
@click.option(
    "--github-token",
    required=True,
    type=click.Path(),
    help="Text file which contains your Github token",
)
@click.option(
    "--to-csv", default=False, is_flag=True, help="Convert output to CSV instead"
)
def main(github_token: str, to_csv: bool) -> None:
    """
    Prints results to STDOUT
    """
    token_fp = Path(github_token)
    assert token_fp.exists(), "Token filepath doesnt exist"
    gh_token = token_fp.read_text().strip()
    client = construct_client(github_token=gh_token)

    printer = csv_printer if to_csv else json_printer

    owned_repos: JsonList = query_results(client=client, gh_query=query_owned())
    contributed_repos: JsonList = query_results(
        client=client, gh_query=query_contributed_to()
    )

    printer(list(chain(owned_repos, contributed_repos)))


def query_results(client: Client, gh_query: gql) -> JsonList:
    return list(exhaust_github_query(client, gh_query))


if __name__ == "__main__":
    main()
