from mkvpy.Tracks.track import Track
from pathlib import Path


class Audio(Track):
    def __init__(
        self,
        file_path: str | Path,
        id: int,
        name: str = "",
        language: str = "",
        default: bool = False,
        forced: bool = False,
        sync: int = 0,
        
        # flags
        original: bool = False,
        visual_impaired: bool = False,
        commentary: bool = False,
    ):
        super().__init__(file_path, id, name, language, default, forced, sync)
        

    def channels(self):
        return self.info_track.get("properties", {}).get("audio_channels", 0)
    def frequency(self):
        return self.info_track.get("properties", {}).get("audio_sampling_frequency", 0)

    def __repr__(self):
        return f"<Audio id={self.id} language={self.language} channels={self.channels} codec={self._id}>"
