from dataclasses import asdict, dataclass

@dataclass(frozen=True)
class CandidateHit:
    target_id: str
    start: int          # zero-based inclusive
    end: int            # zero-based exclusive
    mismatches: int
    guide: str
    target_window: str

    def to_dict(self):
        return asdict(self)
