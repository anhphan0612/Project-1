from dataclasses import dataclass


@dataclass
class AppConfig:
    source_language: str = "en"
    target_language: str = "vi"

    capture_interval_ms: int = 150
    ocr_confidence_threshold: float = 0.5

    enable_frame_diff: bool = True
    enable_translation_cache: bool = True