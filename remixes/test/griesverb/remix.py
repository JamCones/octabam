"""Minimal image for GRIESVERB's gate: the module alone, no stock effect listed."""
from remix.schema import Proof, Remix
REMIX = Remix(family="effects", proof=Proof.RENDER, proof_note="`verify_griesverb`; not flashed", name="griesverb",
              doc="GRIESVERB alone: the fixture of its render gate.",
              modules=("GRIESVERB",), fallback="NONE")
