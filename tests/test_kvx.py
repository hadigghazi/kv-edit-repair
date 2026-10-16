"""CPU tests of the benchmark builder and the edit-time word index (no torch, no model, no API)."""
import importlib.util
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("kvx", ROOT / "extension" / "kvx.py")
kvx = importlib.util.module_from_spec(_spec)
sys.modules["kvx"] = kvx
_spec.loader.exec_module(kvx)

TOK = kvx.StubTok()
POOL = kvx.load_filler_synth()


def _items(cell, n=10):
    return [kvx.make_item(cell, seed, POOL, TOK) for seed in range(n)]


def test_every_cell_builds_length_preserving_items():
    for cell in kvx.ALL_CELLS:
        for it in _items(cell):
            view = kvx.token_view(it, TOK)
            assert view is not None, f"{it['id']}: edit not length-preserving or not inside the edited sentence"
            assert len(view["ids_old"]) == len(view["ids_new"])
            assert it["text_old"].count(it["edit_old"]) == 1 and it["text_new"].count(it["edit_new"]) == 1


def test_direct_items_do_not_leak_the_new_answer():
    for it in _items("direct"):
        assert it["ans_new"] not in it["text_old"]


def test_index_finds_every_explicit_dependent():
    for cell in kvx.CELLS:
        if cell == "direct":
            continue
        recall = [kvx.graph_quality(it, kvx.index_graph(it))[0] for it in _items(cell)]
        assert statistics.mean(recall) == 1.0, cell


def test_index_cannot_follow_paraphrased_links():
    for cell in kvx.CELLS_INDIRECT:
        recall = [kvx.graph_quality(it, kvx.index_graph(it))[0] for it in _items(cell)]
        assert statistics.mean(recall) == 0.0, cell


def test_three_hop_index_reaches_the_second_stage():
    it = kvx.make_item("hop3", 1, POOL, TOK)
    reached = set(kvx.index_graph(it))
    second = {i for i, s in enumerate(it["sentences"]) if s["role"] == "dep1"}
    assert second and second <= reached


def test_row_order_is_randomised():
    flags = [it["new_first"] for it in _items("derived_d250", 30)]
    assert any(flags) and not all(flags)
