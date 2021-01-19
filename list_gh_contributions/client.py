from typing import Optional, Any, Dict, List

from gql import Client, gql  # type: ignore[import]
from gql.transport.requests import RequestsHTTPTransport  # type: ignore[import]

from . import Json, JsonList

GITHUB_GRAPHQL_ENDPOINT = "https://api.github.com/graphql"


def construct_client(
    github_token: str, endpoint_url: str = GITHUB_GRAPHQL_ENDPOINT
) -> Client:
    transport = RequestsHTTPTransport(
        url=GITHUB_GRAPHQL_ENDPOINT,
        verify=True,
        retries=3,
        headers={"Authorization": "token {}".format(github_token)},
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client


def execute_query(client: Client, query: gql, after: Optional[str] = None) -> Json:
    variables = {}
    if after is not None:
        variables["after"] = after
    res: Json = client.execute(query, variable_values=variables)
    return res


# returns all pages for some query
def exhaust_github_query(client: Client, query: gql) -> JsonList:
    results: List[Dict[str, Any]] = []
    continue_paginating = True
    after: Optional[str] = None
    while continue_paginating:
        pagination_results = execute_query(client, query, after=after)
        # the repositories key here only happens to match, wouldnt if this was extended
        # to do lots more graphql queries
        res = extract_content_from_response(pagination_results)
        page_info = res["pageInfo"]
        continue_paginating = page_info["hasNextPage"]
        if continue_paginating:
            after = page_info["endCursor"]
        results.extend(res["nodes"])
    return results


# flatten graphql response into a common list format
def extract_content_from_response(results: Json) -> Any:
    res = results["viewer"]
    # move one level down (repositories or repositoriesContributedTo)
    assert (
        len(res.keys()) == 1
    ), "Couldnt extract shared key/model from graphql response"
    key = list(res.keys())[0]
    res = res[key]
    return res
