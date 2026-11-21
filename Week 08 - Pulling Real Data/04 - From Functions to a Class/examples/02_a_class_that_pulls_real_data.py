"""
A CLASS THAT PULLS REAL DATA
================================
Putting Topics 1-4 together: a class that fetches from a real API and
reports on what it gets back. The lab's DataFetcher class has the same shape.
Run:  python 02_a_class_that_pulls_real_data.py
"""

import requests


class RepoWatch:
    """Pulls an org's repos from the GitHub API and flags noisy ones."""

    def __init__(self, org, issue_limit=1000):
        self.org = org
        self.issue_limit = issue_limit
        self.repos = []
        self.flagged_count = 0

    def fetch(self, count=5):
        """Pull the org's most recently updated repos."""
        url = f"https://api.github.com/orgs/{self.org}/repos"
        response = requests.get(url, params={"per_page": count, "sort": "updated"}, timeout=10)
        response.raise_for_status()
        self.repos = response.json()

    def is_flagged(self, repo):
        """A repo is flagged if it has more open issues than self.issue_limit."""
        return repo["open_issues_count"] > self.issue_limit

    def report(self):
        """Fetch if needed, then print a line per repo and a summary."""
        if not self.repos:
            self.fetch()
        for repo in self.repos:
            flagged = self.is_flagged(repo)
            marker = "FLAGGED" if flagged else "ok"
            print(f"{repo['name']:<20} {repo['open_issues_count']:>6}  {marker}")
            if flagged:
                self.flagged_count += 1
        print(f"\n{self.flagged_count} of {len(self.repos)} flagged")


watch = RepoWatch("python", issue_limit=1000)
watch.report()


# --- Notice what self buys you here ------------------------------------
# fetch(), is_flagged() and report() never pass org, issue_limit or repos
# to each other as arguments - they all reach them through self. Compare
# this to Week 3, where every function needed everything passed in
# explicitly, every time.


# --- TRY IT ------------------------------------------------------------------
# 1. Create a RepoWatch for a different org (e.g. "psf" or "django") and
#    call .report() on it.
# 2. Add a method average_issues(self) that returns the average open issue
#    count across self.repos.
