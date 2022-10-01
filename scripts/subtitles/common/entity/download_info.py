import dataclasses

from subliminal import Video


@dataclasses.dataclass
class DownloadInfo:
    media_name: str
    url: str
    postprocess_status: str
    group: str
    category: str
    report_number: str
    job_name: str
    original_nzb_name: str
    directory: str
    script_name: str
    video: Video = dataclasses.field(init=False)

    def __post_init__(self):
        self.video = Video.fromname(self.media_name)
