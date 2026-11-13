from hypothesis import given, strategies as st
from processor import process_age, process_name, process_scores


@given(st.one_of(st.integers(), st.text(), st.none()))
def test_process_age(age):
    try:
        process_age(age)
    except Exception:
        assert False, f"process_age crashed with input: {age}"


@given(st.one_of(st.text(), st.none(), st.integers()))
def test_process_name(name):
    try:
        process_name(name)
    except Exception:
        assert False, f"process_name crashed with input: {name}"


@given(st.lists(st.integers()))
def test_process_scores(scores):
    try:
        process_scores(scores)
    except Exception:
        assert False, f"process_scores crashed with input: {scores}"