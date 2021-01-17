"""
Queries in this module have a shared 'after' query,
which lets Graphql paginate
"""

from gql import gql  # type: ignore[import]


query_contributed_to: gql = gql(
    r"""query ($after: String) {
  viewer {
    repositoriesContributedTo(first: 100, after: $after, contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]) {
      totalCount
      nodes {
        name
        licenseInfo {
            name
        }
        description
        stargazers {
          totalCount
        }
        primaryLanguage {
          name
        }
        url
        updatedAt
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
}
"""
)


query_owned: gql = gql(
    r"""query ($after: String) {
 viewer {
    repositories(
      first: 100,
      after: $after,
      orderBy: { field: UPDATED_AT, direction: DESC }
    ) {
      nodes {
        name
        licenseInfo {
            name
        }
        description
        stargazers {
          totalCount
        }
        primaryLanguage {
          name
        }
        url
        updatedAt
      }
      pageInfo {
        endCursor
        hasNextPage
      }
    }
  }
}"""
)
