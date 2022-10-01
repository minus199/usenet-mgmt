import logging

from babelfish import Language
from subliminal import AsyncProviderPool

from common.data.secrets import to_config
from common.entity.download_info import DownloadInfo

providers = ['argenteam', 'legendastv', 'opensubtitles', 'opensubtitlesvip', 'podnapisi', 'shooter', 'thesubdb', 'tvsubtitles']
langs = {Language('eng')}


def fetch_subs(metadata):
    logging.info("Fetching subs")

    downloaded_subtitles = {}
    with AsyncProviderPool(max_workers=4, providers=providers, provider_configs=to_config()['provider_configs']) as p:
        subs_list = p.list_subtitles(metadata.video, langs - metadata.video.subtitle_languages)
        subtitles = p.download_best_subtitles(subs_list, metadata.video, langs)
        downloaded_subtitles[metadata.video] = subtitles

    return downloaded_subtitles


def main():
    metadata = DownloadInfo()
    logging.info(metadata)
    subs = fetch_subs(metadata)
    logging.info(subs)
