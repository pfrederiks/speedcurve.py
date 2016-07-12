"""Url Classes."""
from .models import SpeedCurveCore


class SiteMetadata(SpeedCurveCore):
    """The :class:`SiteMetaData <SiteMetaData>"""

    def _update_attributes(self, metadata):
        self.id = metadata.get('site_id')
        self.name = metadata.get('name')
        self.urls = [self._instance_or_null(UrlMetadata, url)
                     for url in metadata.get('urls')]

    def __repr__(self):
        return '<SiteMetaData ({0}) {1} >'.format(self.id, self.name)


class UrlMetadata(SpeedCurveCore):
    """The :class:`UrlMetaData <UrlMetaData>"""

    def _update_attributes(self, metadata):
        self.id = metadata.get('url_id')
        self.url = metadata.get('url')
        self.label = metadata.get('label')

    def __repr__(self):
        return '<UrlMetadata ({0}) {1} >'.format(self.id, self.url)


class Url(SpeedCurveCore):
    """The :class:`Url <Url>` object."""

    def _update_attributes(self, url):
        self.url = url.get('url')
        self.tests = url.get('tests')

    def __repr__(self):
        return 'Url <speedcurve.urls.Url [{0}]'.format(self.url)
