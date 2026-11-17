"""Tests de la validation de l'URL de SiteInternet."""

from __future__ import annotations

import pytest

from enseigne.site_internet import SiteInternet


def test_url_acceptee():
    assert SiteInternet("https://www.exemple.fr").url == "https://www.exemple.fr"


@pytest.mark.parametrize("url", ["exemple.fr", "ftp://x.fr", "http://", ""])
def test_url_refusee(url):
    with pytest.raises(ValueError):
        SiteInternet(url)
